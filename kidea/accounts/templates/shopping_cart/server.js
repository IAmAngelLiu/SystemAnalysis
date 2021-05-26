/*
功能：檢視本地資料中是否含有指定的物件（商品），根據id
引數：id：商品的標識
*/
function checkObjByPid(id) {
var jsonStr = cookieObj.get("datas");
var jsonObj = JSON.parse(jsonStr);
var isExist = false;
for(var i = 0, len = jsonObj.length; i < len; i  ) {
if(jsonObj[i].pid == id) {
isExist = true;
break;
}
}
return isExist; //return false;
}
/*
功能：更新本地資料
引數：arr 陣列物件
返回一個值：最新的本地轉換後的陣列物件
* */
function updateData(arr) {
var jsonStr = JSON.stringify(arr);
cookieObj.set({
name: "datas",
value: jsonStr
});
jsonStr = cookieObj.get("datas");
return JSON.parse(jsonStr);
}
/*
獲取商品的總數量
返回：數字
*/
function getTotalCount() {
/*迴圈遍歷陣列，獲取每一個物件中的pCount值相加總和*/
var totalCount = 0; //預設為0
var jsonStr = cookieObj.get("datas");
var listObj = JSON.parse(jsonStr);
for(var i = 0, len = listObj.length; i < len; i  ) {
totalCount = listObj[i].pCount   totalCount;
}
return totalCount;
}
/*
更新本地資料根據pid
id:商品的標識
*/
function updateObjById(id, num) {
var jsonStr = cookieObj.get("datas");
var listObj = JSON.parse(jsonStr);
for(var i = 0, len = listObj.length; i < len; i  ) {
if(listObj[i].pid == id) {
listObj[i].pCount = listObj[i].pCount   num;
break;
}
}
return updateData(listObj)
}
/*
獲取本地資料
返回 陣列物件
* */
function getAllData() {
var jsonStr = cookieObj.get("datas");
var listObj = JSON.parse(jsonStr);
return listObj;
}
function deleteObjByPid(id) {
var lisObj = getAllData();
for(var i = 0, len = lisObj.length; i < len; i  ) {
if(lisObj[i].pid == id) {
lisObj.splice(i, 1);
break;
}
}
updateData(lisObj);
return lisObj;
}