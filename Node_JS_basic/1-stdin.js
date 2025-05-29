const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const studentLines = lines.slice(1);
    const students = [];
    studentLines.forEach((line) => {
      const fields = line.split(',');
      if (fields.length >= 4 && fields[0].trim() !== '') {
        students.push({
          firstname: fields[0].trim(),
          lastname: fields[1].trim(),
          age: fields[2].trim(),
          field: fields[3].trim(),
        });
      }
    });
    console.log(`Number of students: ${students.length}`);
    const fieldGroups = {};
    students.forEach((student) => {
      if (!fieldGroups[student.field]) {
        fieldGroups[student.field] = [];
      }
      fieldGroups[student.field].push(student.firstname);
    });
    Object.keys(fieldGroups).forEach((field) => {
      const studentNames = fieldGroups[field];
      console.log(`Number of students in ${field}: ${studentNames.length}. List: ${studentNames.join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;