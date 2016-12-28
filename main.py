#coding=utf-8

# music move to dir with artist and album
# ver 0.1 bata
# by zjz

import eyed3
import os
import sys
import shutil

base_dir = "F:\\Music\\#TMP\\tmp";

def mkdir(path):
	#del frist space
	path=path.strip()
	#del last \
	path=path.rstrip("\\")
	# judg is the path exit or not 
	# exist     True
	# not   False
	isExists=os.path.exists(path)
	if not isExists:
		# if the path not exist create the dir
		print "create path: "+ path + " success"
		# make dir
		os.makedirs(path)
		return True
	else:
		# if it exist don't create, and send a note
		print "the path: "+ path + " already have"
		return False


def GetFileList(dir, fileList):
	newDir = dir
	if os.path.isfile(dir):
		fileList.append(dir.decode('gbk'))
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			#if want ignore some dir please use the code as follow:
			#if s == "xxx":
				#continue
			newDir=os.path.join(dir,s)
			GetFileList(newDir, fileList)  
	return fileList


if __name__ == "__main__": # main function
	for audiofile in GetFileList(base_dir, []): # get all files from path
		print audiofile #audio file path
		audioinfo = eyed3.load(audiofile) #load file
		tmp_ar = audioinfo.tag.artist #show artist
		tmp_al = audioinfo.tag.album #show album
		
		if audioinfo.tag.artist is None:
			tmp_ar='unknown'

		if audioinfo.tag.album is None:
			tmp_al='unknown'

		tmp_artist = tmp_ar.replace('?','').replace('*','').replace('"','').replace('\\','').replace('/','').replace('<','').replace('>','').replace('|','').replace(':','')
		tmp_album = tmp_al.replace('?','').replace('*','').replace('"','').replace('\\','').replace('/','').replace('<','').replace('>','').replace('|','').replace(':','')
		print tmp_album
		mkpath= '%s%s%s%s%s%s' % (base_dir , "\\" , tmp_artist , "\\" , tmp_album , "\\")
		new_name= '%s%s%s%s%s%s%s' % ( base_dir,"\\",tmp_artist,"\\",tmp_album,"\\",os.path.basename(audiofile))
		mkdir(mkpath)
		shutil.move(audiofile,new_name)
		print # print a blank line
