const fs = require('fs');

module.exports = function countStudents(path) {
  let readFile;

  try {
    readFile = fs.readFileSync(path);
  } catch (e) {
    throw new Error('Cannot load the database');
  }

  readFile = readFile.toString().split('\n');
  let students = readFile.filter((value) => value);
  students = students.map((value) => value.split(','));

  console.log(`Number of students: ${students.length - 1}`);
  const obj = {};
  for (const line in students) {
    if (line !== 0) {
      if (!obj[students[line][3]]) {
        obj[students[line][3]] = [];
      }
      obj[students[line][3]].push(students[line][0]);
    }
  }
  delete obj.field;
  for (const key of Object.keys(obj)) {
    console.log(`Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
  }
};
