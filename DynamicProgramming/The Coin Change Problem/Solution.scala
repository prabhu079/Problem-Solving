/*
 * https://www.hackerrank.com/challenges/coin-change/problem
 */
import scala.io.StdIn._
object Solution {
  val pattern=" ".r
 def main(args: Array[String])
 {
   val len=pattern.split(readLine).map(x=>x.toInt)
   val amt=len(0)
   val n=len(1)
   val denom=pattern.split(readLine).map(x=>x.toInt)
   val ways=getWays(amt,denom)
   print(ways)
   
 
 }
  def getWays(n: Int, a: Array[Int]): Long = {
    val l1=a.length
    val arr=Array.ofDim[Long](l1+1,n+1)
    
    for(i<- 1 to l1)
    {
      for(j <- 1 to n)
      {
        if(j-a(i-1)==0)
        {
          arr(i)(j)=arr(i-1)(j)+1
        }
        else if((j-a(i-1))>=0 && arr(i)(j-a(i-1))>0)
        {
           arr(i)(j)=arr(i-1)(j)+arr(i)(j-a(i-1))
        }
        else
        {
          arr(i)(j)=arr(i-1)(j)
        }
          
      }
    }
    arr(l1)(n)
    }
}
