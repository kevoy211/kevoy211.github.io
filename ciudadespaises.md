---


---

<table border="1">
    <tr>
        <th>Ciudad</th>
        <th>Pais</th>  
    </tr>
        {% for ciudadpais in site.data.ciudadespaises %}
            <tr>
                <th>{{ciudadpais.ciudad}}</td>
                <td>{{ciudadpais.pais}}</td>
            </tr>
        {% endfor %}  
</table>