// Script.js
function myFunction() {
	alert("Hello! I am an alert box!");
  }

/*const sortableList =
	document.getElementById("sortable");
let draggedItem = null;

sortableList.addEventListener(
	"dragstart",
	(e) => {
		draggedItem = e.target;
		alert("Hello! I am in dragstart");
		setTimeout(() => {
			e.target.style.display =
				"none";
		}, 0);
});

sortableList.addEventListener(
	"dragend",
	(e) => {
		setTimeout(() => {
			e.target.style.display = "";
			draggedItem = null;
		}, 0);
});

sortableList.addEventListener(
	"dragover",
	(e) => {
		e.preventDefault();
		const afterElement =
			getDragAfterElement(
				sortableList,
				e.clientY);
		const currentElement =
			document.querySelector(
				".dragging");
		if (afterElement == null) {
			sortableList.appendChild(
				draggedItem
			);} 
		else {
			sortableList.insertBefore(
				draggedItem,
				afterElement
			);}
	});

const getDragAfterElement = (
	container, y
) => {
	const draggableElements = [
		...container.querySelectorAll(
			"li:not(.dragging)"
		),];

	return draggableElements.reduce(
		(closest, child) => {
			const box =
				child.getBoundingClientRect();
			const offset =
				y - box.top - box.height / 2;
			if (
				offset < 0 &&
				offset > closest.offset) {
				return {
					offset: offset,
					element: child,
				};} 
			else {
				return closest;
			}},
		{
			offset: Number.NEGATIVE_INFINITY,
		}
	).element;
}; */

const sortableList = document.querySelector(".sortable-list");
const items = document.querySelectorAll(".item");

items.forEach(item => {
	item.addEventListener("dragstart", () => {
		setTimeout(() => item.classList.add("dragging"), 0);
		//alert("Hello! I am an alert box!");
	});
	item.addEventListener("dragend", () => item.classList.remove("dragging"));
});

const initSortableList = (e) => {
	const draggingItem = sortableList.querySelector(".dragging");

	const siblings = [...sortableList.querySelectorAll(".item:not(.dragging)")];

	let nextSibling = siblings.find(sibling => {
		return e.clientY <= sibling.offsetTop + sibling.offsetHeight / 2;
	});

	sortableList.insertBefore(draggingItem, nextSibling);
	console.log(nextSibling);
};
sortableList.addEventListener("dragover", initSortableList);