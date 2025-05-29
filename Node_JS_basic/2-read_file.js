const fs = require('fs');

function countStudents(path) {
  try {
    // Leer el archivo de forma síncrona
    const data = fs.readFileSync(path, 'utf8');
    
    // Dividir en líneas y filtrar líneas vacías
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    // Remover la primera línea (headers)
    const studentLines = lines.slice(1);
    
    // Procesar cada línea para obtener estudiantes válidos
    const students = [];
    studentLines.forEach(line => {
      const fields = line.split(',');
      if (fields.length >= 4 && fields[0].trim() !== '') {
        students.push({
          firstname: fields[0].trim(),
          lastname: fields[1].trim(),
          age: fields[2].trim(),
          field: fields[3].trim()
        });
      }
    });
    
    // Mostrar número total de estudiantes
    console.log(`Number of students: ${students.length}`);
    
    // Agrupar estudiantes por campo
    const fieldGroups = {};
    students.forEach(student => {
      if (!fieldGroups[student.field]) {
        fieldGroups[student.field] = [];
      }
      fieldGroups[student.field].push(student.firstname);
    });
    
    // Mostrar estadísticas por campo
    Object.keys(fieldGroups).forEach(field => {
      const studentNames = fieldGroups[field];
      console.log(`Number of students in ${field}: ${studentNames.length}. List: ${studentNames.join(', ')}`);
    });
    
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;