---


---

<table class="border">
        <tr>
            <th>Ciudad</th>
            <th>Pais</th>  
        </tr>
         {% for ciudadpais in site.data.ciudadespaises %}
            
            <tr>
                <td>{{ciudadpais.ciudad}}</td>
                <td>{{ciudadpais.pais}}</td>
            </tr>
        {% endfor %}   
</table>