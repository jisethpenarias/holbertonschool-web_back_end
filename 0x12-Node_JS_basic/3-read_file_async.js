const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
        return;
      }
      const readFile = data.toString().split('\n');
      let students = readFile.filter((value) => value);
      students = students.map((value) => value.split(','));
      const response = [];
      let message;
      message = `Number of students: ${students.length - 1}`;
      console.log(message);
      response.push(message);
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
        message = `Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`;
        console.log(message);
        response.push(message);
      }
      resolve(response);
    });
  });
};
