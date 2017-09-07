#!/usr/bin/env python
import requests
import json
import re
import optparse

class Pizilla:
	def __init__(self):
		self.BASE_URL = 'http://172.16.45.95/'
		self.API_ENDPOINT = 'files/'
		self.FILE_PATH = 'view/'
		self.pat = re.compile(r'\s+')

	def download_all(self):
		response = requests.get(self.BASE_URL + self.API_ENDPOINT)
		if response.ok:
			json_data = json.loads(response.content)
			download_list = self.get_download_list(json_data)
			self.download_files(download_list)
		else:
			print 'download failed!'

	def download_some_files(self, file_list):
		file_list_mod = []

		for file in file_list:
			file_name = re.sub(self.pat, '%20', file)
			file_list_mod.append(file_name)
			self.download_files(file_list_mod)

	def list_files(self):
		response = requests.get(self.BASE_URL + self.API_ENDPOINT)
		if response.ok:
			json_data = json.loads(response.content)
			list_of_files = ""
			for item in json_data:
				file_name = item['name']
				list_of_files += file_name + '\n'
			print list_of_files
			print 'Total number of files present: ' + str(len(json_data))
		else:
			print 'list could not be fetched'

	def get_download_list(self, json_data):
		download_list = []
		
		for item in json_data:
			file_name = item['name']
			file_name = re.sub(self.pat, '%20', file_name)
			download_list.append(file_name)

		return download_list

	def download_files(self, file_list):
		for file in file_list:
			file_url = self.BASE_URL + self.FILE_PATH + file
			print file_url
			try:
			    file_data = requests.get(file_url)
			    if file_data.ok:
				    file_data = file_data.content
				    self.write_to_file(file, file_data)
			    else:
				    print file.replace('%20', ' ') + " could not be downloaded!"
			except:
				print file.replace('%20', ' ') + " could not be downloaded!"

	def write_to_file(self, file_name, file_data):
		file = open(file_name.replace('%20', ' '), 'w')
		file.write(file_data)
		file.close()

if __name__ == '__main__':
	pizilla = Pizilla()

	parser = optparse.OptionParser()
	parser.add_option('-a', '--all', dest='all', action='store_true', help='Download all files')
	parser.add_option('-f', '--files', dest='files', help='Enter file names. File names should be under quotes. Multiple files should be separated by space')
	parser.add_option('-l', '--list', dest='list', action='store_true', help='List all files')

	(options, args) = parser.parse_args()

	if options.all:
		print 'downloading all files...'
		pizilla.download_all()
		exit(0)

	if options.files:
		print 'downloading files...'
		pizilla.download_some_files(options.files.split())
		exit(0)

	if options.list:
		print 'fetching list of files present...'
		pizilla.list_files()
		exit(0)
