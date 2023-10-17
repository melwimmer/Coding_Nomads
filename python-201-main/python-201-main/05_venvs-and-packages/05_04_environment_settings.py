# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

#What I did:
#Create new environment but not activate it
#Went to the bin -> activate script
#Once in there, I under deactivate I unset my variable:
#deactivate () {
#   unset MY_SUPER_SECRET_SECRET
    # Lots of other code
#}

#And at the bottom, I wrote the varable like so:
# #The rest of the script
#export MY_SUPER_SECRET_SECRET="OMG this is so secret I can't even say!"
#and then I activated it, and once active, I did printenv
#and it showed the new variables.
#once deactivated again, the varables are no longer there 