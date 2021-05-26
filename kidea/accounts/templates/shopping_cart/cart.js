/*
思路：
第一步：當頁面載入完後，根據本地的資料，動態生成表格（購物車列表）
獲取所要操作的節點物件
判斷購物車中是否有資料？
有：
顯示出購物列表
沒有：
提示購物車為空
第二步：當購物車列表動態生成後，獲取tbody裡所有 的checkeBox標籤節點物件，看那個被選中就獲取對應行小計進行總價格運算。
第三步：
為每一個checkbox新增一個onchange事件，根據操作更改總價格
第四步：全選
第五步：
為加減按鈕新增一個滑鼠點選事件
更改該商品的數量
第六步：刪除
獲取所有的刪除按鈕
為刪除按鈕新增一個滑鼠點選事件
刪除當前行，並更新本地資料
*/
var listObj = getAllData();
var table = document.getElementById("table")
var box = document.getElementById("box")
var tbody = document.getElementById("tbody");
var totalPrice = document.getElementById("totalPrice");
var allCheck = document.getElementById("allCheck");
if(listObj.length == 0) { //購物車為空
box.className = "box";
table.className = "hide";
} else {
box.className = "box hide";
table.className = "";
for(var i = 0, len = listObj.length; i < len; i  ) {
var tr = document.createElement("tr");
tr.setAttribute("pid", listObj[i].pid);
//{"pid":值,"pImg":值,"pName":值,"pDesc":值,"price":值,"pCount":1},
tr.innerHTML = '<td>'  
'<input type="checkbox" class="ck" />'  
'</td>'  
'<td>'  
'<img src="'   listObj[i].pImg   '" alt="" />'  
'</td>'  
'<td>'  
listObj[i].pDesc  
'</td>'  
'<td>'  
'<button class="down">-</button><input type="text" value="'   listObj[i].pCount   '" readonly="readonly" /><button class="up"> </button>'  
'</td>'  
'<td>'  
'￥<span>'   listObj[i].price   '</span>'  
'</td>'  
'<td>'  
'￥<span>'   listObj[i].price * listObj[i].pCount   '</span>'  
'</td>'  
'<td>'  
'<button class="del" >刪除</button>'  
'</td>';
tbody.appendChild(tr);
}
}
/*
功能：計算總價格
*/
var cks = document.querySelectorAll("tbody .ck");
function getTotalPrice() {
cks = document.querySelectorAll("tbody .ck");
var sum = 0;
for(var i = 0, len = cks.length; i < len; i  ) {
if(cks[i].checked) { //如果當前被選中
var tr = cks[i].parentNode.parentNode;
var temp = tr.children[5].firstElementChild.innerHTML;
sum = Number(temp)   sum;
}
}
return sum;
}
/*迴圈遍歷為每一個checkbox新增一個onchange事件*/
for(var i = 0, len = cks.length; i < len; i  ) {
cks[i].onchange = function() {
checkAllChecked();
totalPrice.innerHTML = getTotalPrice();
}
}
/*全選實現*/
allCheck.onchange = function() {
if(this.checked) {
for(var i = 0, len = cks.length; i < len; i  ) {
cks[i].checked = true;
}
} else {
for(var i = 0, len = cks.length; i < len; i  ) {
cks[i].checked = false;
}
}
totalPrice.innerHTML = getTotalPrice();
}
var downs = document.querySelectorAll(".down"); //一組減的按鈕
var ups = document.querySelectorAll(".up"); //一組加的按鈕
var dels = document.querySelectorAll(".del"); //一組刪除按鈕
for(var i = 0, len = downs.length; i < len; i  ) {
downs[i].onclick = function() {
var txtObj = this.nextElementSibling;//下一個兄弟節點
var tr = this.parentNode.parentNode;
var pid = tr.getAttribute("pid");
txtObj.value = txtObj.value - 1;
if(txtObj.value < 1) {
txtObj.value = 1;
updateObjById(pid, 0)
} else {
updateObjById(pid, -1)
}
tr.children[0].firstElementChild.checked = true;
checkAllChecked();
var price = tr.children[4].firstElementChild.innerHTML;
tr.children[5].firstElementChild.innerHTML = price * txtObj.value;
totalPrice.innerHTML = getTotalPrice();
}
ups[i].onclick = function() {
var txtObj = this.previousElementSibling;//上一個兄弟節點
var tr = this.parentNode.parentNode;
var pid = tr.getAttribute("pid");
txtObj.value = Number(txtObj.value)   1;
updateObjById(pid, 1)
tr.children[0].firstElementChild.checked = true;
checkAllChecked()
var price = tr.children[4].firstElementChild.innerHTML;
tr.children[5].firstElementChild.innerHTML = price * txtObj.value;
totalPrice.innerHTML = getTotalPrice();
}
dels[i].onclick = function() {
var tr = this.parentNode.parentNode;
var pid = tr.getAttribute("pid")
if(confirm("確定刪除？")) {
//remove() 自殺
tr.remove();
listObj = deleteObjByPid(pid);
}
if(listObj.length == 0) { //購物車為空
box.className = "box";
table.className = "hide";
} else {
box.className = "box hide";
table.className = "";
}
totalPrice.innerHTML = getTotalPrice();
}
}
/*檢測是否要全選*/
function checkAllChecked() {
var isSelected = true; //全選是否會選中
for(var j = 0, len = cks.length; j < len; j  ) {
if(cks[j].checked == false) {
isSelected = false;
break;
}
}
allCheck.checked = isSelected;
}