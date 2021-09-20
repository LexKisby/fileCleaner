Basic script to collect files by extension, and group into folders

Works either in the current directory, or the downloads folder, however path to downloads folder will need to be adjusted to work. 

2 modes, strict or not, strict just deletes .zip files. 

existing folders are ignored.

Probably only works on windows, but uses os.path.join() so should be portable

