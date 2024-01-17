import threading
import zipfile


# Define a class AsyncZip that inherits from threading.Thread
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        # Initialize the thread
        threading.Thread.__init__(self)
        # Set the file to zip and the output file name
        self.infile = infile
        self.outfile = outfile

    # Define the code that runs on this thread
    def run(self):
        # Open the ZIP file in write mode with compression
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        # Write the infile to the ZIP file
        f.write(self.infile)
        # Close the ZIP file
        f.close()
        # Print a message when done
        print('Finished background zip of:', self.infile)


# Create an instance of the AsyncZip thread
background = AsyncZip('mydata.txt', 'myarchive.zip')
# Start the thread (calls the run method)
background.start()
# Print a message from the main thread
print('The main program continues to run in foreground.')

# Wait for the background thread to finish
background.join()
# Print a message once the background thread is finished
print('Main program waited until background was done.')
