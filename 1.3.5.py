#HTML
<h1 style="color: blue;"> Заголовок будет синим, т.к. цвет задан в атрибуте style </h1>
<p hidden> Атрибут hidden скрывает элемент на странице, элемент не будет показываться </p>
<button disabled> Кнопка с атрибутом disabled будет заблокирована </button>

#CSS
button {
  background-color: #6c6; 
  border: none;
  color: white;
  padding: 15px 30px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}