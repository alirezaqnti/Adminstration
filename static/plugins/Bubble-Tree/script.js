// am4core.useTheme(am4themes_animated);

// var chart = am4core.create("chartdiv", am4plugins_forceDirected.ForceDirectedTree);

// var series = chart.series.push(new am4plugins_forceDirected.ForceDirectedSeries())

// series.data = [{
//   name: 'Google',
//   children: [{
//     name: 'Maps', value: 1
//   }, {
//     name: 'Drive', value: 1
//   }, {
//     "name": "Chrome",
//     "value": 5,
//     "image": "https://s3-us-west-2.amazonaws.com/s.cdpn.io/t-160/icon_chrome.svg"
//   }, {
//     name: 'Gmail', value: 1
//   }, {
//     name: 'Translate', value: 1
//   }]
// }, {
//   name: 'Meta',
//   children: [{
//     name: 'Facebook', value: 1
//   }, {
//     name: 'Instagram', value: 1
//   }, {
//     name: 'Whatsapp', value: 1
//   }, {
//     name: 'Workplace', value: 1
//   }]
// }, {
//   name: 'Amazon',
//   children: [{
//     name: 'Shopping', value: 1
//   }, {
//     name: 'Video', value: 1
//   }, {
//     name: 'Music', value: 1
//   }, {
//     name: 'Gmail', value: 1
//   }]
// }, {
//   name: 'Apple',
//   children: [{
//     name: 'Store', value: 1
//   }, {
//     name: 'Music', value: 1
//   }]
// }]

// series.dataFields.linkWith = "linkWith";
// series.dataFields.name = "name";
// series.dataFields.id = "name";
// series.dataFields.value = "value";
// series.dataFields.children = "children";
// series.links.template.distance = 1;
// series.links.template.strength = 1;
// series.nodes.template.tooltipText = "{name}";
// series.nodes.template.fillOpacity = 1;
// series.nodes.template.outerCircle.strokeOpacity = 0;
// series.nodes.template.outerCircle.fillOpacity = 0;

// series.nodes.template.label.valign = "bottom";
// series.nodes.template.label.fill = am4core.color("#000");
// series.nodes.template.label.dy = 10;
// series.nodes.template.tooltipText = "{name}: [bold]{value}[/]";
// series.fontSize = 10;
// series.minRadius = 30;
// series.maxRadius = 30;

// series.nodes.template.label.text = "{name}"
// series.fontSize = 8;
// series.minRadius = 15;
// series.nodes.template.label.hideOversized = true;
// series.nodes.template.label.truncate = true;
// series.centerStrength = 1.5;
// series.manyBodyStrength = -2.5;
// series.links.template.strokeOpacity = 0;

// var icon = series.nodes.template.createChild(am4plugins_bullets.PinBullet);
//             icon.image = new am4core.Image();
//             icon.image.propertyFields.href = "image";
//             icon.circle.radius = am4core.percent(100);
//             icon.circle.strokeWidth = 0;
//             icon.background.pointerLength = 0;
//             icon.background.disabled = true;

// series.centerStrength = 0.2;

// am5.ready(function () {
// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
var root = am5.Root.new("chartdiv");

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([am5themes_Animated.new(root)]);

var data = {
  name: "Root",
  value: 0,
  children: [
    {
      name: "توسعه",
      linkWith: ["2"],
      children: [
        {
          name: "A",
          children: [
            { name: "A1", value: 1 },
            { name: "A2", value: 1 },
            { name: "A3", value: 1 },
            { name: "A4", value: 1 },
            { name: "A5", value: 1 },
          ],
        },
        {
          name: "B",
          children: [
            { name: "B1", value: 1 },
            { name: "B2", value: 1 },
            { name: "B3", value: 1 },
            { name: "B4", value: 1 },
            { name: "B5", value: 1 },
          ],
        },
        {
          name: "C",
          children: [
            { name: "C1", value: 1 },
            { name: "C2", value: 1 },
            { name: "C3", value: 1 },
            { name: "C4", value: 1 },
            { name: "C5", value: 1 },
          ],
        },
      ],
    },
    {
      name: "2",
      linkWith: ["3"],
      children: [
        {
          name: "D",
          value: 1,
        },
        {
          name: "E",
          value: 1,
        },
      ],
    },
    {
      name: "3",
      children: [
        {
          name: "F",
          children: [
            { name: "F1", value: 1 },
            { name: "F2", value: 1 },
            { name: "F3", value: 1 },
            { name: "F4", value: 1 },
            { name: "F5", value: 1 },
          ],
        },
        {
          name: "H",
          children: [
            { name: "H1", value: 1 },
            { name: "H2", value: 1 },
            { name: "H3", value: 1 },
            { name: "H4", value: 1 },
            { name: "H5", value: 1 },
          ],
        },
        {
          name: "G",
          children: [
            { name: "G1", value: 1 },
            { name: "G2", value: 1 },
            { name: "G3", value: 1 },
            { name: "G4", value: 1 },
            { name: "G5", value: 1 },
          ],
        },
      ],
    },
  ],
};

// Create wrapper container
var container = root.container.children.push(
  am5.Container.new(root, {
    width: am5.percent(100),
    height: am5.percent(100),
    layout: root.verticalLayout,
    tooltip: am5.Tooltip.new(root, {
      labelHTML: "<button>Click</button>",
      keepTargetHover: true,
    }),
  })
);

// Create series
// https://www.amcharts.com/docs/v5/charts/hierarchy/#Adding
var series = container.children.push(
  am5hierarchy.ForceDirected.new(root, {
    singleBranchOnly: false,
    downDepth: 1,
    topDepth: 1,
    maxRadius: 50,
    minRadius: 12,
    valueField: "value",
    categoryField: "name",
    childDataField: "children",
    idField: "name",
    linkWithStrength: 0.3,
    linkWithField: "linkWith",
    manyBodyStrength: -15,
    centerStrength: 1,
  })
);
// container.events.on("click", function (ev) {
//   console.log("Clicked on a bullet!", ev.target);
// });
series.nodes.template.setAll({
  draggable: false,
});
series.get("colors").set("step", 3);

series.data.setAll([data]);
series.set("selectedDataItem", series.dataItems[0]);
// Make stuff animate on load
series.appear(1000, 100);
// });
container.children.events.on("click", function (e) {
  console.log("Clicked on a column", e.target);
});

// clear children
// root.container.children.clear();
