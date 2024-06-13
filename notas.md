---


---

<table border="2">
    <tr>
        <th>Nombre</th>
        <th>Notas</th>
        <th>Sexo</th>   
    </tr>
        {% for nota in site.data.notas %}
            <tr>
                <td>{{nota.nombre}}</td>
                <td>{{nota.notas}}</td>
                <td>{{nota.sexo}}</td>
            </tr>
        {% endfor %}  
</table>