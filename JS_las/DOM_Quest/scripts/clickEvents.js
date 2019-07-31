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

console.log("Running Click Events Script");

const box1Button = document.getElementById('box1')
const box2Button = document.getElementById('box2')
const box3Button = document.getElementById('box3')

box1Button.addEventListener('click', (e) => {
  box2Button.style.backgroundColor = "red";
  box3Button.style.backgroundColor = "red";
  box1Button.style.backgroundColor = "red";

});

box2Button.addEventListener('click', (e) => {
  box3Button.style.backgroundColor = "pink";
  box1Button.style.backgroundColor = "pink";
  box2Button.style.backgroundColor = "pink";

});

box3Button.addEventListener('click', (e) => {
  box2Button.style.backgroundColor = "orange";
  box3Button.style.backgroundColor = "orange";
  box1Button.style.backgroundColor = "orange";
});
