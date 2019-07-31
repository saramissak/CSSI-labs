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

let currentlily = 1;

const frogger = document.getElementById('frog');

frogger.addEventListener('click', (e) => {
  console.log('hop');
  frogger.style.left = "33.5%";
  frogger.style.top = "23.5%";
  document.getElementById('lilypad2').className = 'lilypad active'
  document.getElementById('lilypad1').className = 'lilypad'
});

frogger.addEventListener('mouseover', (e) => {
  frogger.style.width = '80px';
  frogger.style.height = '80px';
});
frogger.addEventListener('mouseout', (e) => {
  frogger.style.width = '70px';
  frogger.style.height = '70px';
});


document.body.onkeyup = function(e){
    if(e.keyCode == 32){
      document.getElementById('lilypad1').className = 'lilypad active'
      document.getElementById('lilypad2').className = 'lilypad'
      frogger.style.left = "17%";
      frogger.style.top = "50%";
    }
}
