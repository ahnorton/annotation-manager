# Annotation manager
Keep your PDF collection clean by saving Okular annotations to separate files. Requires Python 3.

## Installation
Download the latest release (zip or tar.gz) and extract. E.g. one of,
```
unzip annotation-manager-1.0.zip
```
```
tar xf annotation-manager-1.0.tar.gz
```
The extraction will create directory ./annotation-manager-1.0 (or similar, depending on version number). 
The following scripts need to be made executable,
```
cd annotation-manager-1.0
chmod +x annotation-mgr
chmod +x annotation-ctrl
chmod +x start-annotation-ctrl.sh
```
To test, run the command
```
annotation-ctrl
```
This will start annotation-mgr and create a one button GUI to stop/start annotation-mgr.

Using Okular, add some annotations to a PDF and Save them. Use the button to toggle display of 
the annotations. Note that while annotations are not being displayed (i.e., while annotation-mgr 
is not running) the PDF file is the original, e.g., same size and modification time.

To enable annotation-ctrl to automatically start when KDE starts, see 'annotation-ctrl --help'.  

## To remove/uninstall
Delete the downloaded files and remove the hidden data directory ~/.annotation-manager, 
```
rm -rf ~/.annotation-manager
```
## annotation-mgr  --help
```
 annotation-mgr is a python script that runs in the background to keep your PDF collection
                clean by saving annotations to separate files.

                Annotation manager currently works with the Okular PDF viewer on the KDE desktop.

 Usage:         annotation-mgr is most conveniently started and stopped using annotation-ctrl. 
                See: annotation-ctrl --help.
 
 Description:   Annotations are the highlights, underlines, text notes, free-hand lines, etc.,
                with which users can mark-up a PDF while reading or reviewing it.

                Until about 2018, Okular saved PDF annotations in separate files without modifying
                the PDF file. Nowadays, Okular appends its annotation data to the PDF file.

                The purpose annotation-mgr is to simulate the old Okular behaviour for new Okular 
                versions. While annotation manager is running, Okular appears to behave as though
                it saves annotations to separate files, leaving original PDF files un-modified.

                This effect is achieved as follows. Annotation manager watches the list of PDF 
                files that are currently being viewed by Okular:

                --  when a new PDF appears on this list its file is immediately backed up. If the
                    PDF has a saved annotation file then its contents is appended to the PDF file
                    being viewed, so as to display the saved annotations.

                --  when a PDF drops off the list of PDFs being viewed its original file is 
                    restored from its backup. Any difference between the file and its backup is 
                    saved as a separate annotation file.
               
                The net effect can be summarised as follows: while not being used by Okular, a
                PDF file is always an unmodified original. While being viewed, the PDF file is an
                annotated "working copy" that will differ from the original if annotations have 
                been saved for that PDF.

 Configuration: The PDF viewer must be configured to automatically reload the PDF file when its
                contents change. For Okular, this configuation setting is found at,

                    Settings -> Configure Okular -> General -> Reload document on file change

 Rename, move,  The file in which annotation data is saved is named with the sha256 hash of the
 and copy       contents of the PDF file. The original PDF can thereby be renamed, moved, and 
                copied, without annotations being lost.
                              
                It is best not to rename, move, or copy a PDF file while it is being managed, 
                because you will be operating on the "working copy" rather than the original file.

 Save:          When the Save feature of Okular is used, annotation manager will detect if the 
                working copy of the PDF has been modified and will extract and save the file  
                difference as a separate annotation file. 

 SaveAs:        The SaveAs feature of Okular creates a new PDF file. This new PDF will contain
                what you see -- it will include any annotations that are being displayed. Sometimes
                this is what is wanted. For example, if wanting to send an annotated PDF to be 
                printed, or to a colleague by email.

                Annotation-manager will manage the newly created PDF file just as it does any other
                original PDF. In other words, any further annotations (beyond those which are now
                intrinsic to the newly created PDF) will be saved to a separate annotation file.  

                SaveAs, when used to over-write the displayed PDF file, is equivalent to Save.  

 Web browser:   If your web browser is configured to open PDFs using Okular then annotations can be
                saved and displayed for an online PDF regardless of whether or not not a local copy
                is saved. (This is possible because annotations are associated by sha256 hash 
                with the PDF file contents.)
                  
                When a online PDF is opened by Okular the file that is initially being viewed is
                downloaded to /tmp or a Downloads directory specified by your browser settings.
                To save a local copy one uses the SaveAs feature of Okular. In light of how SaveAs
                works, if clean PDFs are wanted then one should make it a habit to use SaveAs 
                before making annotations. 

                If one forgets the above advice and makes annotations before using SaveAs, then one
                can proceed as follows: 
 
                (1) Save your annotations for all edited PDFs (those with '*' in window titles).  
                (2) Click "Stop" in annotation-ctrl to turn off displaying of annotations. 
                (3) Use SaveAs to save a clean copy of the downloaded PDF.
                (4) Click "Start" in annotation-ctrl to resume displaying saved annotations. 
                  
 Options:       -h, --help      prints this documentation then exits.     

                -v, --version   prints version number then exits.    

                -i, --info      prints information about how to transition from the old-syle .xml
                                annotations to those saved by annotation_mgr, then exit. 

                                Also prints referencs to historical information on the Okular 
                                development decision to change from .xml annotations.

                -d, --debug     will output messages about what is being done. This is useful 
                                for understanding the inner workings of annotation-manager.
                             
                -e, --exclude   exclude management of PDFs that have filenames matching a pattern.
                                Example:  
                                          annotation-mgr --exclude '*_tex/selection.pdf'
  
                                Pattern matching uses the python function fnmatch.fnmatchcase().
                                                
                -f, --files     prints the list of files that are being displayed by Okular,
                                excluding those specified by the --exclude option, then exits.

 Locations:     All annotation data that is saved by annotation-mgr and annotation-ctrl is under
                ~/.annotation-manager.

 Author:        Andrew H. Norton (norton.ah@gmail.com)

 Licence:       CC0. 
```
## annotation-mgr  --info
```
    Earlier versions of Okular used to save annotations in human readable and easily searchable
    .xml files in directory
    
        ~/.kde/share/apps/okular/docdata/

    These .xml files were named according to the size and name of the orginal PDF file, with 
    names of the form
    
                   <PDF size>.<PDF filename>.xml
    
    Annotations were therefore lost if PDF files were renamed, but not lost if simply moved from
    one directory to another. The PDF size was used to help prevent name clashes. 

    The same file naming convention is currently used to save the .xml files that record viewing
    data (window size, page number, etc.) to the directory

        ~/.local/share/okular/docdata/

    Saving separate annotations was removed as of KDE Applications 17.12.

    Okular nowadays saves annotations by appending the annotation data to the PDF file. The 
    annotation files created by annotation-mgr are the PDF file differences. These are not human
    readable nor are they easily searchable. They are named by the sha256 hash of the original 
    PDF file contents, so do not get lost if the original PDF is renamed, moved, or copied.

    Transitioning from old .xml annotation files:

        When Okular opens a PDF that has annotation data saved in the old .xml format, a banner
        is displayed,

            "This document contains annotations or form data that were saved internally by a 
             previous Okular version. Internal storage is no longer supported. Please save to
             a file in order to move them if you want to continue to edit the document."

        By "internal" the above message obscurely means internal to Okular's hidden data 
        directories, rather than internal to the PDF. 

        The banner is displayed with a SaveAs button. While annotation-mgr is running, use that
        SaveAs option to overwrite the PDF file.       

        The .xml annotations will be saved (as a PDF file difference) by annotation-mgr and the
        .xml file will be deleted by Okular. The banner will not be displayed again.         

    For pros/cons and discussion: 
        
        The following dates are those of the first post. Many comments on these posts have been
        made some years later. 

        2007-10-31 store annotations with documents 
        https://bugs.kde.org/show_bug.cgi?id=151614 

        2011-03-15 Okular should display a warning about before annotating 
        https://bugs.kde.org/show_bug.cgi?id=268575

        2014-09-07 Survey about "Save As" and "Save" features
        https://forum.kde.org/viewtopic.php?t=122750

        2017-??-?? --- separate .xml annotations removed from Okular.

        2017-10-01 Storing Okular PDF annotations in a separate file
        https://forum.kde.org/viewtopic.php?f=251&t=141963

        2018-05-28 Annotations in the separated XML files 
        https://bugs.kde.org/show_bug.cgi?id=394775 
 
        2018-07-20 Save annotations internally (docdata) 
        https://bugs.kde.org/show_bug.cgi?id=396681

        2018-08-02 .okular archive should store the original file 
        https://bugs.kde.org/show_bug.cgi?id=397097
```
## annotation-ctrl  --help
```
 annotation-ctrl is a single button GUI for annotation-mgr that toggles displaying or not 
                 displaying PDF annotations that have been saved by annotation-mgr.

                 The command 'annotation-ctrl' starts annotation-mgr (if not running) and also 
                 displays a single button GUI for starting and ending the annotation-mgr process.
                 
                 Closing the annotation-ctrl GUI will also end the annotation-mgr process.

                 See: annotation-mgr --help  

 Usage:          Typically annotation-ctrl would be started automatically after KDE starts. This
                 can be achieved using ~/.config/autostart-scripts. The file,

                      start-annotation-ctrl.sh 

                 is an autostart script. See the comments in that file for how to install it.    

 Options:        -h, --help      will print this documentation then exit.     

                 -v, --version   will print the version number then exit. 

                 -e, --exclude   passed to annotation_mgr. See: annotation-mgr --help 

                 -d, --debug     passed to annotation_mgr. See: annotation-mgr --help  
```
