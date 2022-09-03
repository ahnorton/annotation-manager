# annotation-manager
Keep your PDF collection clean by saving annotations to separate files.

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
                versions. While annotation manager is running, Okular appears to behave as though it 
                saves annotations to separate files, leaving original PDF files un-modified.

                This effect is achieved as follows. Annotation manager watches the list of PDF files
                that are currently being viewed with Okular:

                --  when a new PDF appears on this list its file is immediately backed up. If the PDF
                    has a saved annotation file then its contents is appended to the PDF file being 
                    viewed, so as to display the saved annotations.

                --  when a PDF drops off the list of PDFs being viewed its original file is restored 
                    from its backup. Any difference between the file and its backup is saved as a 
                    separate annotation file.
               
                The net effect can be summarised as follows: while not being used by the PDF viewer,
                a PDF file is always an unmodified original. While being viewed, the PDF file is an 
                annotated "working copy" that will differ from the original if annotations have been 
                saved for that PDF.

 Configuration: The PDF viewer must be configured to automatically reload the PDF file when its
                contents change. For Okular, this configuation setting is found at,

                    Settings -> Configure Okular -> General -> Reload document on file change

 Rename, move,  The file in which annotation data is saved is named with the sha256 hash of the
 and copy       contents of the PDF file. The original PDF can thereby be renamed, moved, and copied, 
                without annotations being lost.
                              
                It is best not to rename, move, or copy a PDF file while it is being managed, because 
                you will be operating on the "working copy" rather than the original file.                           

 Save:          When the Save feature of Okular is used, annotation manager will detect if the 
                working copy of the PDF has been modified and will extract and save the file  
                difference as a separate annotation file. 

 SaveAs:        The SaveAs feature of Okular creates a new PDF file. This new PDF will contain
                what you see -- it will include any annotations that are being displayed. Sometimes 
                this is what is wanted. For example, if wanting to send an annotated PDF to a printer, 
                or to a colleague by email.

                Annotation-manager will manage this newly created PDF file just as it does any other
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
                works, if clean PDFs are wanted then one should make it a habit to use SaveAs before 
                making annotations. 

                If one forgets the above advice and makes annotations before using SaveAs, then one 
                can proceed as follows: 
 
                (1) Save your annotation edits for all PDFs (those with '*' in their window titles).  
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

 Licence:       CC0 
