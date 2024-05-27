---


---

<table>
        {% for ciudadpais in site.data.ciudadespaises %}
            <tr>
                <th>Ciudad</th>
                <th>Pais</th>  
            </tr>
            <tr>
                <td>{{ciudadpais.ciudad}}</td>
                <td>{{ciudadpais.pais}}</td>
            </tr>
        {% endfor %}   
</table>