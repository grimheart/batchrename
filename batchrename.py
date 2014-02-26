import sys, os, shutil, fnmatch, glob, subprocess, platform
from PyQt4 import QtCore, QtGui
from ui_batchrename import Ui_BatchRename


class PreviewTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent = None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.table = [[]]

    def rowCount(self, parent):
        return len(self.table)

    def columnCount(self, parent):
        max = 0
        for y in self.table:
            ly = len(y)
            if ly > max:
                max = ly
        return max

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return (self.table[index.row()][index.column()])

    def setData(self, index, value):
        self.table[index.row()][index.column()] = value
        return True

    #def insertRows(x, y, index):

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def clear(self):
        self.table = [[]]


class BatchRename(QtGui.QWidget):
    def __init__(self):
        super(BatchRename, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_BatchRename()
        self.ui.setupUi(self)

        # Set the frameless window hint
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Default config
        self.count      = 0
        self.subdir     = "renamed"
        self.safety     = True
        self.basename   = "file"
        self.padding    = 3
        self.startAt    = 1
        self.fileFilter = "*.jpg *.jpeg *.tif *.tiff *.png *.raw *.gif"

        try:
            self.directory = sys.argv[1]
        except:
            self.directory = os.path.expanduser("~")

        # Fill in defaults on the interface
        self.setBasename()
        self.setDirectory()

        # Redraw relevant elements
        self.updatePreview()

        # Show the window
        self.show()

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


    def pad(self, num):
        u'Zero-pad the given number by the current value of self.padding'

        return str(num).zfill(self.padding)

    def setBasename(self):
        u'Set the basename input box to match the current self.basename'

        self.ui.basenameInput.setText(self.basename)

    def setDirectory(self):
        u'Set the directory input box to match the current self.directory'

        self.ui.directoryInput.setText(self.directory)

    def outputDir(self):
        u'Return the output dir for the current directory'

        return os.path.join(self.directory, self.subdir)

    def genFilename(self, path):
        u'Generate the next filename given the current settings and self.count'

        ext  = os.path.splitext(path)[1]
        name =  self.basename + "-" + self.pad(self.count+self.startAt-1) + ext
        return name

    def relativeFilename(self, path):
        u'Return the current output filename relative to the output directory'

        return os.path.join(self.subdir, self.genFilename(path))

    def renameFile(self, path):
        u'Return the full path to the current filename'

        return os.path.join(self.outputDir(), self.genFilename(path))

    def updatePreview(self):
        u'Update the targets list and the preview list interface elements'

        files = self.listFiles()

        row = 0
        for path in files:
            item = QtGui.QTableWidgetItem(path)
            self.ui.previewTable.setItem(row, 0, item)
            row += 1

        self.count = 0
        for path in files:
            self.count += 1
            path = os.path.join(self.subdir, self.genFilename(path))

            if os.path.exists(os.path.join(self.directory, path)):
                path = ["[x]", path]
            else:
                path = ["[ ]", path]

            item_s = QtGui.QTableWidgetItem(path[0])
            item_p = QtGui.QTableWidgetItem(path[1])
            self.ui.previewTable.setItem(self.count-1, 1, item_s)
            self.ui.previewTable.setItem(self.count-1, 2, item_p)

        if os.path.exists(self.outputDir()):
            self.ui.outputButton.setEnabled(True)
            self.ui.cleanupButton.setEnabled(True)
        else:
            self.ui.outputButton.setEnabled(False)
            self.ui.cleanupButton.setEnabled(False)

    def filterFile(self, path):
        u'Return true if the given path points to a file'

        return os.path.isfile(os.path.join(self.directory, path))

    # Courtesy http://www.peterbe.com/plog/uniqifiers-benchmark
    def uniq(self, seq):
        u'Return only the unique members of the given sequence'

        seen = {}
        result = []
        for item in seq:
            if item in seen: continue
            seen[item] = 1
            result.append(item)
        return result

    def listFiles(self):
        u'Return a list of files in self.directory matching the current filter'

        files = []
        for extglob in self.fileFilter.split(" "):
            fullglob = os.path.join(self.directory, extglob)
            files += glob.glob(fullglob)
        files = self.uniq(files)
        return [ f for f in files if self.filterFile(f) ]


    def rename(self):
        u'Rename the targeted files'

        files = self.listFiles()
        try:
            shutil.rmtree(self.outputDir())
        except:
            pass
        try:
            os.mkdir(self.outputDir())
        except:
            pass
        self.count = 0
        for f in files:
            self.count += 1
            r = self.renameFile(f)
            fabs = os.path.join(self.directory, f)
            rabs = os.path.join(self.outputDir(), r)
            shutil.copyfile(fabs, rabs)
        self.updatePreview()

    def changeDirectory(self):
        u'Set the target directory from the contents of the directory input box'

        self.directory = str(self.ui.directoryInput.text())
        self.updatePreview()

    def browseDirectory(self):
        u'Open a file browser to select a new target directory'

        browse = QtGui.QFileDialog(self)
        browse.setDirectory(self.directory)
        browse.setFileMode(QtGui.QFileDialog.Directory)
        if (browse.exec_()):
            self.directory = str(browse.selectedFiles()[0])
            self.ui.directoryInput.setText(self.directory)
            self.updatePreview()

    def changeBasename(self):
        u'Update the basename setting to match the basename input box'

        self.basename = str(self.ui.basenameInput.text())
        self.updatePreview()

    def updateFilter(self):
        u'Update the file filter setting to match the filter input box'

        self.fileFilter = str(self.ui.filterInput.text())
        self.updatePreview()

    def updatePadding(self):
        u'Update the padding setting to match the padding input box'

        self.padding = int(self.ui.paddingInput.text())
        self.updatePreview()

    def updateStart(self):
        u'Update the start-at setting to match the "count from" input box'

        self.startAt = int(self.ui.startAtInput.text())
        self.updatePreview()

    def toggleSafety(self):
        u'Enable or disable the rename button'

        self.safety = not self.safety
        if self.safety:
            self.ui.renameButton.setEnabled(True)
        else:
            self.ui.renameButton.setEnabled(False)

    def openOutputDir(self):
        u'Open the directory containing the renamed files'

        if os.path.exists(self.outputDir()):
            platformType = platform.system()
            if platformType == "Linux":
                subprocess.Popen(["xdg-open", self.outputDir()])
            elif platformType == "Windows":
                subprocess.Popen(["start", self.outputDir()], shell=True)

    def cleanup(self):
        u'Remove the output directory if it exists'

        try:
            shutil.rmtree(self.outputDir())
        except:
            pass
        self.updatePreview()

    def doExit(self):
        u'Exit the program'

        # Call sys.exit instead of exit for MS Windows campatibility
        sys.exit()


def main():
    u'Ye olde canonical entry point'

    app = QtGui.QApplication(sys.argv)
    br  = BatchRename()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

