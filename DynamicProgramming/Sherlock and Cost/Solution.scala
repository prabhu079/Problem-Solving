import scala.io.StdIn._
import math._

object Solution {
  val pattern = " ".r
  def main(args: Array[String]) {
    val t = readLine.trim.toInt
    for (i <- 1 to t) {
      val n = readLine.trim.toInt
      val arr = pattern.split(readLine).map(_.toInt)
      val res = cost(arr)
      println(res)
    }
  }
  def cost(arr: Array[Int]): Int = {
    var hi = 0
    var low = 0
    for (i <- 1 until arr.length) {
    val highToLowDiff = abs(arr(i-1) - 1)
		val lowToHighDiff = abs(arr(i) - 1)
		val highToHighDiff = abs(arr(i) - arr(i-1))
		
		val lowNext = max(low, hi+highToLowDiff)
		val hiNext = max(hi+highToHighDiff, low+lowToHighDiff)
		
		low = lowNext
		hi = hiNext
    }
    max(low,hi)
  }
}
