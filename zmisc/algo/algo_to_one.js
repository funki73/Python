/*
  Sum To One Digit
  Implement a function sumToOne(num)​ that,
  given a number, sums that number’s digits
  repeatedly until the sum is only one digit. Return
  that final one digit result.
  Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function sumToOneDigit(num) {
  var numstring = num.toString()
    if (numstring.length == 0){
        return 0
    }
    return parseInt(numstring[0]) + sumToOneDigit(numstring.slice(1))
  }

console.log(sumToOneDigit(111))

module.exports = { sumToOneDigit };

/*****************************************************************************/

// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129
/* 
  String Anagrams

  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).

  Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// // Order of the output array does not matter

// /**
//  * Add params if needed for recursion.
//  * Generates all anagrams of the given str.
//  * - Time: O(?).
//  * - Space: O(?).
//  @param {string} str
//  @returns {Array<string>}
//  */
function generateAnagrams(str) {}

module.exports = { generateAnagrams };