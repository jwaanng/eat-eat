let itineraryForm = document.querySelector('#itinerary-form')
console.log(itineraryForm)

let numQuestionsTextForm = document.getElementById('num-questions')
console.log(numQuestionsTextForm.value)

let questionSection = document.getElementById('question-section')
console.log(questionSection)

let generateQuestionsSection = document.getElementById('generate-questions')
console.log(generateQuestionsSection)

generateQuestionsSection.addEventListener('click', event => {
    event.preventDefault();

    const numQuestions = parseInt(numQuestionsTextForm.value);
    console.log(numQuestions)
    
    let questionsHtml = '';
    for (let i = 0; i < numQuestions; i++) {
      questionsHtml += `
        <div id="question-section">
        <label for="price">Place ${i+1}: What type of place would you like to go?</label>
        <select multiple class="form-control" id="price">
            <option>Cafe</option>
            <option>Dessert</option>
            <option>Dinner</option>
            <option>Drinks</option>
            <option>Fast Food</option>
            <option>Lunch</option>
            <option>Doesn't Matter</option>
            <option>No More</option>
        </select>
        </div>
      `;
    }
    questionSection.innerHTML = questionsHtml;
  });