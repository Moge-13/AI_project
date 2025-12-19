function printStatus(id: number, status: "pending" | "done") {
  console.log(`Task ${id} is ${status}`);
}

printStatus(1, "pending");
printStatus(2, "done");
