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

// Use querySelector to store the div in a variable.
const redButton = document.querySelector('#red');
const greenButton = document.querySelector('#green');
const blueButton = document.querySelector('#blue');
const box = document.getElementById("response-box");
let word = '';
const clearButton = document.getElementById('clear');
// Use addEventListener to respond to a click event.
redButton.addEventListener('click', (e) => {
  console.log("You clicked the red button!");
  box.style.backgroundColor = "red";
  word += 'red ';
  box.innerHTML = word;
});

clearButton.addEventListener('click', (e) => {
  console.log("You clicked the clear button!");
  word = '';
  box.innerHTML = word;
  box.style.backgroundColor = "white";

});

greenButton.addEventListener('click', (e) => {
  console.log("You clicked the red green!");
  box.style.backgroundColor = "green";
  word += 'green ';
  box.innerHTML = word;
});
blueButton.addEventListener('click', (e) => {
  console.log("You clicked the red blue!");
  box.style.backgroundColor = "blue";
  word += 'blue ';
  box.innerHTML = word;
});
