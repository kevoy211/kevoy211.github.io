---


---

<table border="1">
        <tr>
            <th>Ciudad</th>
            <th>Pais</th>  
        </tr>
        <tr>
            {% for ciudadpais in site.data.ciudadespaises %}
                <td>{{ciudadpais.ciudad}}</td>
                <td>{{ciudadpais.pais}}</td>
            {% endfor %}
        </tr>   
</table>