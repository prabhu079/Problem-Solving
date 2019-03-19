/*
 * https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem
 */
import scala.io.StdIn._
object Solution {
  val pattern = " ".r
  def main(args: Array[String]): Unit =
    {
      val len = pattern.split(readLine).map(x => x.toInt)
      val n = len(0)
      val m = len(1)
      val arrA = pattern.split(readLine).map(x => x.trim.toInt)
      val arrB = pattern.split(readLine).map(x => x.trim.toInt)
      val res = longestCommonSubsequence(arrA, arrB)
      //res.map(x => print(x+" "))
      val sb=new StringBuilder
      res.addString(sb," ")
      print(sb)
    }

  def longestCommonSubsequence(a: Array[Int], b: Array[Int]): Array[Int] = {
    val lA = a.length
    val lB = b.length

    val arr = Array.ofDim[String](lA + 1, lB + 1).map(_.map(x => ""))
    for (i <- 1 to lA) {
      for (j <- 1 to lB) {
        if (a(i - 1) == b(j - 1)) {
          arr(i)(j) = arr(i - 1)(j - 1) + " " + a(i - 1)
        } else {
          if (arr(i - 1)(j).length() >= arr(i)(j - 1).length()) {
            arr(i)(j) = arr(i - 1)(j)
          } else if (arr(i - 1)(j).length() < arr(i)(j - 1).length()) {
            arr(i)(j) = arr(i)(j - 1)
          }
        }
      }
    }
    pattern.split(arr(lA)(lB).trim).map(x => x.toInt)
  }
}
