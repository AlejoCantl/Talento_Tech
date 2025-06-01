db.Estudiantes.insertMany([
    { nombre: "Juan", edad: 20, ciudad: "Bogotá" },
    { nombre: "Ana", edad: 22, ciudad: "Medellín" },
    { nombre: "Luis", edad: 19, ciudad: "Cali" }
  ]);

// Todos los documentos
db.Estudiantes.find();

// Filtrando por ciudad
db.Estudiantes.find({ ciudad: "Medellín" });

// Estudiantes mayores de 20 años
db.Estudiantes.find({ edad: { $gt: 20 } });