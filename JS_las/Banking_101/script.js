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

let customerName;
let balance;
let loggedIn = false;
let password;

var pass = prompt("Whats your password?: ")

console.log(openAccount("Sara", 300, pass))

function logIn(name, pass){
  user_name =prompt("What is your name? ");
  user_pass = prompt("What is your password? ");
  if(user_name == customerName && user_pass == password){
    loggedIn = true;
    return customerName + " has logged in."
  }
  return "Incorrect log in"
}

function logOut(){
  loggedIn = false;
  return customerName + " has logged out."
}
function openAccount(name, starting = 0, password) {
  balance = starting;
  password = password;
  customerName = name;

  return name + " has opened a new account with a balance of $" + starting + "."

};

const deposit = (value) => {
  if(loggedIn===true){
    balance = balance + value;
    return customerName + " has deposited $"+value+". "+customerName+ "'s total balance is $"+balance;
  };
  return "User must log in."
}
  console.log(deposit(50))


const withdraw = (draw) => {
  if(loggedIn===true){
    if (balance >= draw){
      balance = balance - draw;
      return customerName +" has withdrawn "+draw+". "+customerName+" has $"+balance+" remaining."
    }

    return   "Sorry, "+customerName+", you do not have enough money in your account. You need "+(draw-balance)+" more dollars."
  };
  return "User must log in."

};
console.log(withdraw(500))


// Write your script below
