ymaps.ready(initMap);
let center = [55.353657, 86.147167]
function initMap() {
    let map = new ymaps.Map('My-map', {
        center: center,
        zoom: 16.2
    });

    let placemark = new ymaps.Placemark(center, {
        balloonContent:'' +
            '<div class="balloon">' +
            '<div class="balloon__address">Московский просп., 11, Кемерово</div>'+
            '<div class="balloon__contacts"><a href="tel+7(900)056-95-90">+7(900)056-95-90</a></div>' +
            '<div class="balloon__schedule">Часы работы: 10:00-20:00</div>'+
            '</div>          '
        // balloonContentHeader: 'хедер балуна',
        // balloonContentBody: 'боди балуна',
        // balloonContentFooter: 'футер балуна',
    }, {
        iconLayout:'default#image',
        iconImageHref: '../static/images/map/pin.png',
        iconImageSize: [40, 40],
        iconImageOffset: [-25, -35],

    });

  map.controls.remove('geolocationControl'); // удаляем геолокацию
  map.controls.remove('searchControl'); // удаляем поиск
  map.controls.remove('trafficControl'); // удаляем контроль трафика
  map.controls.remove('typeSelector'); // удаляем тип
  map.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
  map.controls.remove('zoomControl'); // удаляем контрол зуммирования
  map.controls.remove('rulerControl'); // удаляем контрол правил
  map.behaviors.disable(['scrollZoom']); // отключаем скролл карты (опционально)

    map.geoObjects.add(placemark);

}
