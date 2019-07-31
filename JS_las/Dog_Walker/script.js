// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Task 1
const dogName1 = "Steve";
const dogType1 = "beagle";

console.log("I will walk" + dogName1 +  " today at 12:00pm");



const dogName2 = "Joe";
const dogType2 = "corgi";

if(dogType2 === "corgi"){
  console.log("I will walk " +dogName2+ " today at 12:00pm");
} else {
  console.log("I will walk " +dogName2 +" today at 1:00pm");
}


const dogName3 = "Lola";
const dogType3 = "bulldog";

if(dogType3 === "corgi" || dogType3 === "beagle"){
  console.log("I will walk " +dogName3+ " today at 12:00pm");
} else if(dogType3 === "bulldog"){
  console.log("I will walk " +dogName3 +" today at 1:00pm");
} else {
  console.log("I will walk "+dogName3+" today at 2:00pm")
}

let dogOwner;
let time = null;
if(dogName3.ignoreCase == "Lola".ignoreCase || dogName3.ignoreCase == "Jeremy".ignoreCase){
  if(dogType3.ignoreCase === "corgi".ignoreCase || dogType3.ignoreCase === "beagle".ignoreCase){
    time = "12:00pm";
  } else if(dogType3 === "bulldog"){
    time ="1:00pm";
  } else {
    time ="2:00pm";
  }
  console.log("I will walk " +dogName3  +", one of my favorite dogs, today at" +time + ".");
}
  else{
    if(dogType3 === "corgi" || dogType3 === "beagle"){
      console.log("I will walk " +dogName3+ " today at 12:00pm");
    } else if(dogType3 === "bulldog"){
      console.log("I will walk " +dogName3 +" today at 1:00pm");
    } else {
      console.log("I will walk "+dogName3+" today at 2:00pm")
    }
  }
