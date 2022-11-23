#!\bin\sh
read -p "enter a number" n
for((i=2;i<$n/2;i++))
do
  if [ $((n%i)) -eq 0 ]
  then
echo "$n is not a prime no"
exit 
fi
done
echo "$n is prime no "

