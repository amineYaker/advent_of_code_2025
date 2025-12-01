package day1;
import scala.io.Source

object Main:

  def setup(input: List[String]): List[Int] =
    input.map(command =>
      (if command.head == 'L' then -1 else 1) * command.tail.toInt
    )

  def part1(data: List[Int]): Long = data
    .foldLeft((50, 0)) { case ((position, count), turn) =>
      (
        (position + turn) % 100,
        count + (if ((position + turn) % 100 == 0) 1 else 0)
      )
    }
    ._2

  def part2(moves: List[Int]): Long =
    rotate(moves, 50, 0)

  def rotate(moves: List[Int], initialPosition: Int, res: Int): Int =
    moves match
      case Nil => res
      case head :: tail =>
        val newPosition = Math.floorMod(initialPosition + head, 100)
        val turned: Boolean =
          head > 0 && initialPosition + (head % 100) >= 100 || head < 0 && initialPosition > 0 && initialPosition + (head % 100) <= 0
        val additionalRes = head.abs / 100 + (if turned then 1 else 0)
        rotate(tail, newPosition, res + additionalRes)

  def main(args: Array[String]): Unit =

    val input: List[String] =
      Source.fromFile("input.txt").getLines().toList
    val data = setup(input)
    // val res = part1(data)
    val res = part2(data)

    println(res)
