for var in "$@"
do
  docker-compose -f docker-compose.yml build $var;
  docker-compose -f docker-compose.yml up -d $var;
done
