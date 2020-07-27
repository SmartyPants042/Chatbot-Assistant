# # SETUP WORKING PATH
# # find the shell name
# shell_name=$(echo $SHELL | cut -d '/' -f 4)
# # go to the profile
# ~/.$shell_name
# # add this
# export PYTHONPATH="${PYTHONPATH}:/path/to/the/base/directory"

# # INSTALLING DEPENDENCIES
# pip3 install -r requirements.txt
# python3 -m nltk.downloader all

# # EXPERIMENTAL DEPENDENCIES
# pip3 install -U spacy
# python3 -m spacy download en_core_web_sm

# echo "SUCCESS!"