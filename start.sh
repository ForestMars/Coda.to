# start.sh - Start up script for Coda.to

## get deployment 
# env = dev 


echo "Sourcing ENV variables"
# source env-dev.sh
# source env-prod.sh
source env.sh


#echo "Initialising Airflow database"
#airflow initdb

#echo "Starting Airflow scheduler" 
#airflow scheduler & 

python run.py 
