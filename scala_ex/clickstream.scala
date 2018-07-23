import scala.sys.process._
val histogram = ( "gzcat datasets/clickstream_sample.tsv.tar.gz" #| "cut -f 10" #| "sort" #|  "uniq -c" #| "sort -k1nr" ).lineStream 

histogram take(10) foreach println

