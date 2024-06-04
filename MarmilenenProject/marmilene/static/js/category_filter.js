$(document).ready(function () {
    function filterServices(category) {
        $(".service").hide();
        if (category === "all") {
            $(".service").show();
        } else {
            $(".service[data-category='" + category + "']").show();
        }
    }

    function updateActiveClass(category) {
        $(".category-link").removeClass("active");
        $(".category-link[data-category='" + category + "']").addClass("active");
    }

    $("#category-selector").on("change", function () {
        var selectedCategory = $(this).val();
        filterServices(selectedCategory);
        updateActiveClass(selectedCategory);
    });

    $(".category-link").on("click", function (e) {
        e.preventDefault();
        var category = $(this).data("category");
        filterServices(category);
        updateActiveClass(category);
    });

    $(".select-header").on("click", function () {
        $(".options").toggleClass("active");
    });

    $(".options div").on("click", function () {
        var selectedValue = $(this).data("value");
        $("#selected-option").text($(this).text());
        $(".options").removeClass("active");
        filterServices(selectedValue);
        updateActiveClass(selectedValue);
    });

    var isInitialLoad = true;

    function setInitialCategory() {
        if (isInitialLoad) {
            isInitialLoad = false;
            var firstCategory = $(".category-link:not(.active)").first().data("category");
            filterServices(firstCategory);
            updateActiveClass(firstCategory);
        }
    }

    setTimeout(function () {
        $(".select-container").addClass("select-visible");
        $(".options").css({ opacity: 1, visibility: "visible", transform: "translateY(0)" });

        // Вызов функции для установки первой категории активной и фильтрации услуг
        setInitialCategory();
    }, 100);

    // Добавьте обработчик события для клика по категории
    $(".category-link").on("click", function (e) {
        e.preventDefault();
        var category = $(this).data("category");
        filterServices(category);
        updateActiveClass(category);
    });

    // Добавьте обработчик события для изменения значения в пользовательском селекте
    $(".options div").on("click", function () {
        var selectedValue = $(this).data("value");
        $("#selected-option").text($(this).text());
        $(".options").removeClass("active");
        filterServices(selectedValue);
        updateActiveClass(selectedValue);
    });
});


