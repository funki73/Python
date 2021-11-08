// // /* 
// // 	Acronyms
// // 	Create a function that, given a string, returns the string’s acronym 
// // 	(first letter of each word capitalized). 
// // 	Do it with .split first if you need to, then try to do it without
// // */

// // // const str1 = " there's no free lunch - gotta pay yer way. ";
// // // const expected1 = "TNFL-GPYW";

// // // const str2 = "Live from New York, it's Saturday Night!";
// // // const expected2 = "LFNYISN";

// // // function acronymize(str) {
// // // 	// str.split(" ");

// // // }

// // /*****************************************************************************/
// // /* 
// // 	String: Reverse
// // 	Given a string,
// // 	return a new string that is the given string reversed
// // */

// // const str1 = "creature";
// // const expected1 = "erutaerc";

// // const str2 = "dog";
// // const expected2 = "god";

// // function reverseString(str) {
// // 	// loop through a string
// // for (var i=str.length-1; i >= 0; i--){
// //     str1 += str[i];
// //     }
// // return str1;
// // }
// // console.log(reverseString(str1))

// // function acronymize(str){
// //     //setup
// // }
// // /********************************************************************************
// // 10/26/2021


// // //SETUP
// // //veriable that holds the new string we are going to build

// // //WORK
// // // loop through the array to the second to last element
// // 	//look through the array
// // 	//et the value from the array
// // 	//add it to the new string
// // 	//add the seperator to the new string

// // //add the final element in teh array to the new string

// // //RETURN
// // 	//return that the new string.                      
// // /********************************************************************************
// //  * funkicryp37
// // #4558

// // [8:52 AM] Instructor_ShawnC: @cohort-ShawnC 🏫 
// // GOOD MORNING!
// // Class starts in 10 minutes! Looking forward to seeing all of you there! If you need the link to the schedule, it is in the description of this channel.
// // [8:53 AM] Instructor_ShawnC:
// // [8:55 AM] Armen_Garayan: Hey Shawn is there a password to the zoom session?
// // [8:55 AM] Michael_Schmidt: Yeah im having trouble too finding it
// // [8:55 AM] Armen_Garayan: Good Morning!
// // [8:55 AM] Instructor_ShawnC: The link should take you to the zoom straight, but the password is under the zoom link on the schedule
// // [8:56 AM] Michael_Hughes: nov_python
// // [9:08 AM] Instructor_JimR:
// // [9:42 AM] Instructor_ShawnC: Hello! Today's algo file! 
// // /* 
// // 	Acronyms
// // 	Create a function that, given a string, returns the string’s acronym 
// // 	(first letter of each word capitalized). 
// // 	Do it with .split first if you need to, then try to do it without
// // */
// // Expand
// // algos.js
// // 1 KB
// // [10:05 AM] Andrew_Schoch:
// // /* 
// //     Acronyms
// //     Create a function that, given a string, returns the string’s acronym 
// //     (first letter of each word capitalized). 
// //     Do it with .split first if you need to, then try to do it without
// // */

// // const str1 = " there's no free lunch - gotta pay yer way. ";
// // const expected1 = "TNFL-GPYW";

// // const str2 = "Live from New York, it's Saturday Night!";
// // const expected2 = "LFNYISN";

// // function acronymize(str) {
// //     str.split(" ");
// //     var result = ''
// //     for( var i =0; i < str.split(' ').length; i++){
// //         result+=str.split(' ')[i].charAt(0).toUpperCase()

// //     } return result
        

// // }

// // console.log(acronymize(str2))

// // /*****************************************************************************/

// // /* 
// //     String: Reverse
// //     Given a string,
// //     return a new string that is the given string reversed
// // */

// // const str1 = "creature";
// // const expected1 = "erutaerc";

// // const str2 = "dog";
// // const expected2 = "god";

// // function reverseString(str) {
// //     // loop through a string
// //     var result =''
// //     for(var i =str.length-1; i>-1; i--){
// //         result+=str.charAt(i)
// //     }
// //     return result
// // }

// // console.log(reverseString(str2))
// // [10:08 AM] Mollie_Houkom: zachary, wei,

// // [10:08 AM] Mollie_Houkom: I just forgot our fourth member, sorry!
// // [10:10 AM] Elysia_Roscoe: @William_Dwelle @Natascha_Haberl @Michael_Hughes @Ken_Watkins @Elysia_Roscoe  we attempted a few different ideas and didn't finish. gave it a good brainstorm though

// // [10:49 AM] Elysia_Roscoe:
// // [12:12 PM] Instructor_ShawnC: Grabbing some lunch! be back soon
// // [1:09 PM] Instructor_ShawnC: i am back!
// // [1:39 PM] MarieMadeleine_Corpin: @Instructor_ShawnC I need assistance/clarification in the Room of Pasta, please? Thanks.
// // [2:06 PM] Elysia_Roscoe: @Instructor_ShawnC I have a syntax question when you have a moment. dont see you in pasta room right now but im in 4 
// // [2:57 PM] Instructor_ShawnC: @cohort-ShawnC 🏫 Afternoon session starting in just a few minutes!
// // [5:34 PM] Instructor_ShawnC: This afternoon's diagram 

// // [6:00 PM] Instructor_ShawnC: Video is linked and is finished up youtube processing. it will be viewable soon 
// // [9:24 AM] Instructor_ShawnC: Good Morning! Here is Tuesday's Algo file!
// // /* 
// //   Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
// //   No trailing separator at the end
// //   Default the separator to a comma with a space after it if no separator is provided
// // */
// // Expand
// // algos.js
// // 3 KB
// // ﻿
// /* 
//   Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
//   No trailing separator at the end
//   Default the separator to a comma with a space after it if no separator is provided
// */

// const arr1 = [1, 2, 3];
// const separator1 = ", ";
// const expected1 = "1, 2, 3";

// const arr2 = [1, 2, 3];
// const separator2 = "-";
// const expected2 = "1-2-3";

// const arr3 = [1, 2, 3];
// const separator3 = " - ";
// const expected3 = "1 - 2 - 3";

// const arr4 = [1];
// const separator4 = ", ";
// const expected4 = "1";

// const arr5 = [];
// const separator5 = ", ";
// const expected5 = "";

// /**
//  * Converts the given array into a string of items separated by the given separator.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<string|number|boolean>} arr The items to be joined as a string.
//  * @param {string} separator To separate each item of the given arr.
//  * @returns {string} The given array items as a string separated by the given separator.
//  */
// function join(arr, separator) {
//   // SETUP
//   // variable that holds the new string we are going to build
// 	var result = ""
//   	for (var x=0; x < arr.length - 1; x++){
// 		result += arr[x] + separator
// 	}
// 	result += arr[arr.length - 1]
// 	return result
//   // WORK
//   // loop through the array to the second to last element
//     // get the value from the array
//     // add it to the new string
//     // add the separator to the new string

//   // add the final element in the array to he new string

//   // RETURN
//   // return the new string
// }
// console.log(join(arr1, separator1))

// /*****************************************************************************/

// /* 
// Book Index
// Given an array of ints representing page numbers
// return a string with the page numbers formatted as page ranges when the nums span a consecutive range
// */

// // const nums1 = [1, 13, 14, 15, 37, 38, 70];
// // const expected1 = "1, 13-15, 37-38, 70";

// /**
//  * Turns the given arr of page numbers into a string of comma hyphenated
//  * page ranges.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums Page numbers.
//  * @returns {string} The given page numbers as comma separated hyphenated
//  *    page ranges.
//  */
// // function bookIndex(nums) {
// // 	var result = ""
// // 	for (var i=0; i < nums.length; i++){
// // 		if (nums [i] + 1 == nums [i + 1]){
// // 			for (var j=i+1; j < nums.length; j++){
// // 				if (nums[j] + 1 != nums[j + 1])
// // 		}
// // 	}
// // }

//   // SETUP
//   // new string that we are going to build

//   // WORK
//   // Loop through the nums array *
//     // check if the next element after the current is a consecutive number e.g. if i = 0, look at i = 1
//       // if that element is consecutive, continue looking ahead until we come across an element that is no longer consecutive
//       // we can use a while loop to continue looking ahead until the numbers are no longer consecutive
//     // add the page numbers to the string
//       // if there was not a consecutive, just add the number and the ", "
//       // if there was a consecutuve, add the first and last of the consecutive numbers, separated by a dash, followed by the ", "


//   // RETURN
//   // return that new string


// /* 
//   Given in an alumni interview in 2021.
//   String Encode
//   You are given a string that may contain sequences of consecutive characters.
//   Create a function to shorten a string by including the character,
//   then the number of times it appears. 
  
  
//   If final result is not shorter (such as "bb" => "b2" ),
//   return the original string.
//   */

//   const str1 = "aaaabbcddd";
//   const expected1 = "a4b2c1d3";
  
//   const str2 = "";
//   const expected2 = "";
  
//   const str3 = "a";
//   const expected3 = "a";
  
//   const str4 = "bbcc";
//   const expected4 = "bbcc";
  
//   /**
//    * Encodes the given string such that duplicate characters appear once followed
//    * by a number representing how many times the char occurs only if the
//    * character occurs more than two time.
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str The string to encode.
//    * @returns {string} The given string encoded.
//    */
//   function encodeStr(str) {
    
//     var newstring = "";
//     var storestring = [];
//     var count = 0;

//     for (var i=0; i < str.length; i++){
//         if (str[i] == str.length - 1){
//           count + 1;
//           newstring += str[i];
//         }
//         storestring.append(newstring, count);
//         count = 0
//       }

//     // SETUP
//     // we need a variable to hold the encoded string we build
//     // variable that stores the currect char in the string
//     // variable to hold the count of characters
  
//     // WORK
//     // loop through the str -
//       // compare the currCharVariable to the char at the current index in the string if it does match -
//         // if they are the same, increase the count of the count varaible -
//       // compare the currCharVarialbe to the char at the current index in the string to see if it doesn't match -
//         // add the currChar and the count to the encoded string
//         // reset the count
//         // set the currCharVariable to the next letter
  
//     // RETURN
//     // compare the lengths of the encoded string to the original
//       // if encoded is shorter, return encoded
//       // if encoded is not shorter, return the original
//   // }
  
//   /*****************************************************************************/
// 10/29

// funkicryp37
// #4558

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
// [10:03 AM] MarieMadeleine_Corpin: @Elysia_Roscoe @Nicholas_Chambers @MarieMadeleine_Corpin  @Armen_Garayan  & Steven Nguyen

// [10:06 AM] Chris_Nguyen:
// const arr1 = [1, 2, 3];
// const separator1 = ", ";
// const expected1 = "1, 2, 3";

// const arr2 = [1, 2, 3];
// const separator2 = "-";
// const expected2 = "1-2-3";

// const arr3 = [1, 2, 3];
// const separator3 = " - ";
// const expected3 = "1 - 2 - 3";

// const arr4 = [1];
// const separator4 = ", ";
// const expected4 = "1";

// const arr5 = [];
// const separator5 = ", ";
// const expected5 = "";

// /**
//  * Converts the given array into a string of items separated by the given separator.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<string|number|boolean>} arr The items to be joined as a string.
//  * @param {string} separator To separate each item of the given arr.
//  * @returns {string} The given array items as a string separated by the given separator.
//  */
// function join(arr, separator) {
//   // SETUP
//   // variable that holds the new string we are going to build
//   var result = "";

//   // WORK
//   // loop through the array to the second to last element
//   for(let i=0; i<arr.length-1; i++){
//     // get the value from the array, add it to the new string and add the separator to the new string
//     result += arr[i] + separator;
//   } 
//   // add the final element in the array to he new string
//   result += arr[arr.length-1];
//   // RETURN
//   return result;
// }
// console.log(join(arr3, separator3))
// [11:51 AM] William_Dwelle: @Instructor_ShawnC can I get some help in room 8?
// [11:55 AM] Natascha_Haberl: hey just wanted to extend an invitation to everyone in the cohort, when we're in breakout rooms you're always free to join me. We usually have a small group going to discuss assignments or go over anything that we're struggling with. We're not all always working on the same assignments but try to help each other as we're going along
// [11:58 AM] Instructor_ShawnC: Heading to lunch!
// [1:54 PM] Mollie_Houkom: @Instructor_ShawnC I have a question in room 7
// [4:57 PM] Instructor_ShawnC: that is it for me today. Have a great evening!
// [9:20 AM] Instructor_ShawnC: Good Morning! Today's algo file!
// /* 
//   Given in an alumni interview in 2021.
//   String Encode
//   You are given a string that may contain sequences of consecutive characters.
//   Create a function to shorten a string by including the character,
//   then the number of times it appears. 
// Expand
// algos.js
// 3 KB
// [10:00 AM] Deana_Canfield:
// const str1 = "aaaabbcddd";
// const expected1 = "a4b2c1d3";

// const str2 = "";
// const expected2 = "";

// const str3 = "a";
// const expected3 = "a";

// const str4 = "bbcc";
// const expected4 = "bbcc";

//   /**
//    * Encodes the given string such that duplicate characters appear once followed
//    * by a number representing how many times the char occurs only if the
//    * character occurs more than two time.
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str The string to encode.
//    * @returns {string} The given string encoded.
//    */
//     function encodeStr(str) {
//         var newString = "";
//         var count = 0;
//         for(var i =0; i <str.length; i++){     /*looping through the */
//             if(str.charAt(i+1)== str.charAt(i)){ /* */
//                 count += 1;
//             }
//             else{
//                 count += 1;
//                 newString += str[i] + count.toString();
//                 count=0;
//             }
//         }
//         if(newString.length == str.length || str.length == 1){
//             return str;
//         }
//         else{
//             return newString;
//         }
//     }

//     console.log(encodeStr(str1))
//     console.log(encodeStr(str2))
//     console.log(encodeStr(str3))
//     console.log(encodeStr(str4))
// [10:00 AM] Natascha_Haberl: My internet crashed brb
// [10:05 AM] Michael_Hughes: @Zachary_Houston @Michael_Schmidt @Elysia_Roscoe

// // [11:37 AM] William_Dwelle: if anyone wants to work together on dojo pets I'm in room 6 feel free to join
// // [1:04 PM] Natascha_Haberl: ahhh i missed this message
// // [3:19 PM] Elysia_Roscoe: Just confirming Algo style we are meant to come up with one game for the entire group
// // [3:19 PM] Instructor_ShawnC: Yes. Everyone works together on one game
// // [5:01 PM] Instructor_ShawnC: Alright, That is it for me.
// // I really do appreciate all the hard work everyone put in today and all that participation during the Hackathon. Keep it up!

// // Have a great night, and I'll see you tomorrow!
// // [5:01 PM] Instructor_ShawnC:
// // [8:53 AM] Elysia_Roscoe: Did anyone else have trouble installing Flask? I tried using the python -m pipenv <command to use> they recommended but i'm still getting a bash syntax error
// // [9:14 AM] Instructor_ShawnC: Good Morning! Algo file for today
// // /* 
// //   String: Is Palindrome
// //   Create a function that returns a boolean whether the string is a strict palindrome. 
// //     - palindrome = string that is same forwards and backwards
  
// //   Do not ignore spaces, punctuation and capitalization
// // Expand
// // algos.js
// // 2 KB
// // [9:21 AM] Deana_Canfield: Hello
// // [9:33 AM] Instructor_ShawnC: hello!
// // [9:33 AM] MarieMadeleine_Corpin: My computer suddenly decided to restart itself... Sorry. Still waiting for it to boot back up.
// // [9:34 AM] MarieMadeleine_Corpin: Typing from the Discord App on my phone…
// // [9:44 AM] Nate_Savage: palindrome code!
// // /* 
// // String: Is Palindrome
// Create a function that returns a boolean whether the string is a strict palindrome. 
// - palindrome = string that is same forwards and backwards

// Do not ignore spaces, punctuation and capitalization
// Expand
// SPOILER_algos_13.js
// 3 KB
// [9:50 AM] Elysia_Roscoe:
// // maps to a value 
// Expand
// algos.js
// 2 KB
// ﻿
// /* // /* 
//     String: Is Palindrome
//     Create a function that returns a boolean whether the string is a strict palindrome. 
//     - palindrome = string that is same forwards and backwards

//     Do not ignore spaces, punctuation and capitalization
// Expand
// algos.js
// 3 KB
// Thread
// thank you
// 1 Message ›
// Elysia_Roscoe
// 23h ago
// [10:54 AM] Elysia_Roscoe: Sorry I’ve been connecting and disconnecting, computer finally crapped out and xfinity admitted there’s an outage

// [11:12 AM] Instructor_ShawnC: @cohort-ShawnC 🏫 
// ITS ACTIVITY DAY!
// Come on by for some jack box party games till noon!
// https://codingdojo.zoom.us/j/82235081915
// Zoom Video
// Join our Cloud HD Video Meeting
// Zoom is the leader in modern enterprise video communications, with an easy, reliable cloud platform for video and audio conferencing, chat, and webinars across mobile, desktop, and room systems. Zoom Rooms is the original software-based conference room solution used around the world in board, conference, huddle, and training rooms, as well as ex...
// [11:19 AM] Deana_Canfield: @everyone it's raid time
// [11:20 AM] William_Dwelle: Anyone is welcome to join me in room 6 if you want to work together!
// [11:20 AM] Natascha_Haberl: ill join after activity time
// [11:48 AM] Instructor_ShawnC: Diagrams from this morning

// [11:48 AM] Instructor_ShawnC:

// [11:49 AM] Instructor_ShawnC: Videos are linked and lecture code is on github
// [11:53 AM] MarieMadeleine_Corpin: Hey @Instructor_ShawnC! Would the Activity Day be recorded so that those who won't be able to attend can watch after?
// [11:53 AM] Instructor_ShawnC: Activity day is not recorded, as its a time for students to hang out away from coding.
// [11:54 AM] MarieMadeleine_Corpin: Ahhh. Okidoke... Will join the next one.
// [1:44 PM] Elysia_Roscoe: Meeting at 3?
// [1:50 PM] Natascha_Haberl: i believe so? i think jim will be taking over though
// [2:15 PM] Weicheng_Lee: i think thyell ping us
// [9:12 AM] Instructor_ShawnC: Happy Friday! Today's Algo file
// /* 
//   Zip Arrays into Map
  
  
//   Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
//   Associative arrays are sometimes called maps because a key (string) 
  // Zip Arrays into Map
  
  
//   Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
//   Associative arrays are sometimes called maps because a key (string) maps to a value 
//  */

/*
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value
*/

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
// const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
// };

function zipArraysIntoMap(keys, values) {
    // SETUP
    var dic = {};
    // WORK
        // loop thru both at the same time
        for (var i = 0; i < keys.length; i++) {
            // key1 index will be key val1 will be the value
            dic[keys[i]] = values[i]
        }
    // RESULT
    return dic
}

console.log(zipArraysIntoMap(keys1, vals1))

/*****************************************************************************/

/*
Invert Hash
A hash table / hash map is an obj / dictionary
Given an object / dict,
return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

function invertObj(obj) {
    // SETUP
    var dic = {}
    var arrayKeys = Object.values(obj);
    var arrayVals = Object.keys(obj);
    // WORK
    dic = zipArraysIntoMap(arrayKeys, arrayVals)
    // RESULT
    return dic
}

console.log(invertObj(obj1))

