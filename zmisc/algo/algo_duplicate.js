/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "abcafaqabcazzAABB";
const expected3 = "abcfqzAB";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
  freqTable = {}
  for(let i = 0; i<str.length; i++){
    let char = str[i]
    if(freqTable.hasOwnProperty(char)){
      freqTable[char] += 1
    } else {
      freqTable[char] = 1
      }
    }
  // if (!freqTable.hasOwnProperty(char)) {
  //   freqTable[char] = true
  //   returnStr += char
  //  }
  console.log(Object.keys(freqTable).join(""))
  // return Object.keys(freqTable).join("")
}
stringDedupe(str1)
stringDedupe(str2)
stringDedupe(str3)

