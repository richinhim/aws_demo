from pyspark import SparkContext

sc = SparkContext('local','SparkDemo')

rdd = sc.textFile("input.txt")

print(rdd.count())