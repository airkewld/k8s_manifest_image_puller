import logging as log
import sys
import getopt
import re

FORMAT = '%(asctime)s %(message)s'
log.basicConfig(format=FORMAT,level=log.INFO)

def main(argv):
   inputfile = ''
   outputfile = 'images'
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      log.info('image-puller.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h","--help"):
         log.info('image-puller.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   image_regex = re.compile(r"(image:|image\":)(.*)")

   try:
     manifest = open(inputfile)
   except FileNotFoundError:
        log.error("No input file provided.")
        sys.exit(2)
   content = manifest.read()
   images = image_regex.findall(content)
   images = sorted(set(images))

   bad_characters = ','

   for image in images:
    for character in bad_characters:
        image=image[1].replace(character,'')
    pulled_image = open(outputfile,"a")
    pulled_image.write(image + "\n")
    pulled_image.close()

main(sys.argv[1:])
