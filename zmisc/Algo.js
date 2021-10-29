// /* 
// 	Acronyms
// 	Create a function that, given a string, returns the string’s acronym 
// 	(first letter of each word capitalized). 
// 	Do it with .split first if you need to, then try to do it without
// */

// // const str1 = " there's no free lunch - gotta pay yer way. ";
// // const expected1 = "TNFL-GPYW";

// // const str2 = "Live from New York, it's Saturday Night!";
// // const expected2 = "LFNYISN";

// // function acronymize(str) {
// // 	// str.split(" ");

// // }

// /*****************************************************************************/
// /* 
// 	String: Reverse
// 	Given a string,
// 	return a new string that is the given string reversed
// */

// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

// function reverseString(str) {
// 	// loop through a string
// for (var i=str.length-1; i >= 0; i--){
//     str1 += str[i];
//     }
// return str1;
// }
// console.log(reverseString(str1))

// function acronymize(str){
//     //setup
// }
// /********************************************************************************
// 10/26/2021


// //SETUP
// //veriable that holds the new string we are going to build

// //WORK
// // loop through the array to the second to last element
// 	//look through the array
// 	//et the value from the array
// 	//add it to the new string
// 	//add the seperator to the new string

// //add the final element in teh array to the new string

// //RETURN
// 	//return that the new string.                      
// /********************************************************************************
//  * funkicryp37
// #4558

// [8:52 AM] Instructor_ShawnC: @cohort-ShawnC 🏫 
// GOOD MORNING!
// Class starts in 10 minutes! Looking forward to seeing all of you there! If you need the link to the schedule, it is in the description of this channel.
// [8:53 AM] Instructor_ShawnC:
// [8:55 AM] Armen_Garayan: Hey Shawn is there a password to the zoom session?
// [8:55 AM] Michael_Schmidt: Yeah im having trouble too finding it
// [8:55 AM] Armen_Garayan: Good Morning!
// [8:55 AM] Instructor_ShawnC: The link should take you to the zoom straight, but the password is under the zoom link on the schedule
// [8:56 AM] Michael_Hughes: nov_python
// [9:08 AM] Instructor_JimR:
// [9:42 AM] Instructor_ShawnC: Hello! Today's algo file! 
// /* 
// 	Acronyms
// 	Create a function that, given a string, returns the string’s acronym 
// 	(first letter of each word capitalized). 
// 	Do it with .split first if you need to, then try to do it without
// */
// Expand
// algos.js
// 1 KB
// [10:05 AM] Andrew_Schoch:
// /* 
//     Acronyms
//     Create a function that, given a string, returns the string’s acronym 
//     (first letter of each word capitalized). 
//     Do it with .split first if you need to, then try to do it without
// */

// const str1 = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";

// const str2 = "Live from New York, it's Saturday Night!";
// const expected2 = "LFNYISN";

// function acronymize(str) {
//     str.split(" ");
//     var result = ''
//     for( var i =0; i < str.split(' ').length; i++){
//         result+=str.split(' ')[i].charAt(0).toUpperCase()

//     } return result
        

// }

// console.log(acronymize(str2))

// /*****************************************************************************/

// /* 
//     String: Reverse
//     Given a string,
//     return a new string that is the given string reversed
// */

// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

// function reverseString(str) {
//     // loop through a string
//     var result =''
//     for(var i =str.length-1; i>-1; i--){
//         result+=str.charAt(i)
//     }
//     return result
// }

// console.log(reverseString(str2))
// [10:08 AM] Mollie_Houkom: zachary, wei,

// [10:08 AM] Mollie_Houkom: I just forgot our fourth member, sorry!
// [10:10 AM] Elysia_Roscoe: @William_Dwelle @Natascha_Haberl @Michael_Hughes @Ken_Watkins @Elysia_Roscoe  we attempted a few different ideas and didn't finish. gave it a good brainstorm though

// [10:49 AM] Elysia_Roscoe:
// [12:12 PM] Instructor_ShawnC: Grabbing some lunch! be back soon
// [1:09 PM] Instructor_ShawnC: i am back!
// [1:39 PM] MarieMadeleine_Corpin: @Instructor_ShawnC I need assistance/clarification in the Room of Pasta, please? Thanks.
// [2:06 PM] Elysia_Roscoe: @Instructor_ShawnC I have a syntax question when you have a moment. dont see you in pasta room right now but im in 4 
// [2:57 PM] Instructor_ShawnC: @cohort-ShawnC 🏫 Afternoon session starting in just a few minutes!
// [5:34 PM] Instructor_ShawnC: This afternoon's diagram 

// [6:00 PM] Instructor_ShawnC: Video is linked and is finished up youtube processing. it will be viewable soon 
// [9:24 AM] Instructor_ShawnC: Good Morning! Here is Tuesday's Algo file!
// /* 
//   Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
//   No trailing separator at the end
//   Default the separator to a comma with a space after it if no separator is provided
// */
// Expand
// algos.js
// 3 KB
// ﻿
/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
  // SETUP
  // variable that holds the new string we are going to build
	var result = ""
  	for (var x=0; x < arr.length - 1; x++){
		result += arr[x] + separator
	}
	result += arr[arr.length - 1]
	return result
  // WORK
  // loop through the array to the second to last element
    // get the value from the array
    // add it to the new string
    // add the separator to the new string

  // add the final element in the array to he new string

  // RETURN
  // return the new string
}
console.log(join(arr1, separator1))

/*****************************************************************************/

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

// const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const expected1 = "1, 13-15, 37-38, 70";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
// function bookIndex(nums) {
// 	var result = ""
// 	for (var i=0; i < nums.length; i++){
// 		if (nums [i] + 1 == nums [i + 1]){
// 			for (var j=i+1; j < nums.length; j++){
// 				if (nums[j] + 1 != nums[j + 1])
// 		}
// 	}
// }

  // SETUP
  // new string that we are going to build

  // WORK
  // Loop through the nums array *
    // check if the next element after the current is a consecutive number e.g. if i = 0, look at i = 1
      // if that element is consecutive, continue looking ahead until we come across an element that is no longer consecutive
      // we can use a while loop to continue looking ahead until the numbers are no longer consecutive
    // add the page numbers to the string
      // if there was not a consecutive, just add the number and the ", "
      // if there was a consecutuve, add the first and last of the consecutive numbers, separated by a dash, followed by the ", "


  // RETURN
  // return that new string


/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs only if the
   * character occurs more than two time.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  function encodeStr(str) {
    
    var newstring = "";
    var storestring = [];
    var count = 0;

    for (var i=0; i < str.length; i++){
        if (str[i] == str.length - 1){
          count + 1;
          newstring += str[i];
        }
        storestring.append(newstring, count);
        count = 0
      }

    // SETUP
    // we need a variable to hold the encoded string we build
    // variable that stores the currect char in the string
    // variable to hold the count of characters
  
    // WORK
    // loop through the str -
      // compare the currCharVariable to the char at the current index in the string if it does match -
        // if they are the same, increase the count of the count varaible -
      // compare the currCharVarialbe to the char at the current index in the string to see if it doesn't match -
        // add the currChar and the count to the encoded string
        // reset the count
        // set the currCharVariable to the next letter
  
    // RETURN
    // compare the lengths of the encoded string to the original
      // if encoded is shorter, return encoded
      // if encoded is not shorter, return the original
  // }
  
  /*****************************************************************************/
  