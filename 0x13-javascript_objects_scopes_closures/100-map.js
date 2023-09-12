#!/usr/bin/node
import {list} from "./100-data.js"

console.log(list);
const newList = list.map((item, index) => item * index)
console.log(newList);
