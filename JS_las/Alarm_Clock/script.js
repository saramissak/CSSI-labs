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

console.log("script is running...");

function alarmMessage(basicAlarm){
  return basicAlarm;
};

console.log(alarmMessage("My alarm!"));

function myAlarm(wakeUpTime) {
  return "Hey, Sara, wake up! It's "+ wakeUpTime+ ".";
};

console.log(myAlarm(8))

function momAlarm(time) {
  return "Hey, Mom, wake up! It's "+ time+ ".";
};

function familyAlarm(person, time){
  return "Hey, " + person + ", wake up! It's "+ time + ".";
};
console.log(familyAlarm("Hunter", 2))

function importantAlarm(message){
  return message.toUpperCase();
}

console.log(importantAlarm("yo what up"))

function snoozeAlarm(num){
  return "The alarm for "+ num +" has been changed to "+ (num +1)+ ".";
};


function snoozeAlarm(num_people) {
  for (i = 0; i < num_people; i++) {
    console.log('Wake up');
  }
}

snoozeAlarm(3);
