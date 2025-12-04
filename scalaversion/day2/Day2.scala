package day2;
import scala.io.Source

object Main:

  def nbDigitsOf(id: Long): Int =
    id.toString.length

  def partSizesOf(id: Long): List[Int] =
    val digits = nbDigitsOf(id)
    (1 to digits / 2).toList.filter(digits % _ == 0)

  def checkPartInValidity(partSize: Int, id: Long): Boolean =
    val strId = id.toString
    val parts = strId.grouped(partSize).toList
    val firstPart = parts.head
    parts.forall(_ == firstPart)

  def isInvalid(id: Long): Boolean =
    partSizesOf(id).exists(partSize => checkPartInValidity(partSize, id))

  def main(args: Array[String]): Unit =

    val input: List[(Long, Long)] =
      Source
        .fromFile("./input.txt")
        .getLines()
        .toList
        .head
        .split(",")
        .map(rng => rng.split("-"))
        .toList
        .map(arr => (arr(0).toLong, arr(1).toLong))
    val idsInRanges: List[Long] =
      input.flatMap { case (start, end) => (start to end).toList }
    val invalidIds: List[Long] =
      idsInRanges.filter(isInvalid)
    // need to convert to Long to avoid overflow
    println(invalidIds.map(_.toLong).sum)
