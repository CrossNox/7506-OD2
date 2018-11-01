
var filas = [];

document.onload = start

function start(json,section){

  const endpoint = json;

  var html = ''

  fetch(endpoint)
  .then(blob => blob.json())
  .then(function(data) {
      return data.map(fila => {
        html +=
        `
          <tr>
              <th scope="row" class="text-center">${fila.anio}</th>
              <td class="text-center">${fila.cuatrimestre}</td>
              <td class="text-center">${fila.oportunidad}</td>
              <td><a href="${fila.resuelto}">${fila.resuelto}</a></td>
              <td><a href="${fila.notebook}">${fila.nombreNotebook}</a></td>
          </tr>
        `;
        document.getElementById('table'+section).innerHTML = html;
      });
  });
}
