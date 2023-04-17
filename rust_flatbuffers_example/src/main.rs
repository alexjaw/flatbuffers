extern crate flatbuffers;

mod monster_generated;
pub use monster_generated::my_game::sample::{
    Color, Equipment,
    Monster, MonsterArgs,
    Vec3, Weapon, WeaponArgs};

mod myschema_generated;
pub use myschema_generated::users::{
    User, UserArgs
};

mod classification_generated;
pub use classification_generated::dnn_vision::{
    GeneralClassification, GeneralClassificationArgs,
    ClassificationData, ClassificationDataArgs,
    ClassificationTop, ClassificationTopArgs
};

fn monster() {
    // Build up a serialized buffer algorithmically.
    // Initialize it with a capacity of 1024 bytes.
    let mut builder = flatbuffers::FlatBufferBuilder::with_capacity(1024);

    // Serialize some weapons for the Monster: A 'sword' and an 'axe'.
    let weapon_one_name = builder.create_string("Sword");
    let weapon_two_name = builder.create_string("Axe");

    // Use the `Weapon::create` shortcut to create Weapons with named field
    // arguments.
    let sword = Weapon::create(&mut builder, &WeaponArgs{
        name: Some(weapon_one_name),
        damage: 3,
    });
    let axe = Weapon::create(&mut builder, &WeaponArgs{
        name: Some(weapon_two_name),
        damage: 5,
    });

    // Name of the Monster.
    let name = builder.create_string("Orc");

    // Inventory.
    let inventory = builder.create_vector(&[0u8, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

    // Create a FlatBuffer `vector` that contains offsets to the sword and axe
    // we created above.
    let weapons = builder.create_vector(&[sword, axe]);

    // Create the path vector of Vec3 objects:
    //let x = Vec3::new(1.0, 2.0, 3.0);
    //let y = Vec3::new(4.0, 5.0, 6.0);
    //let path = builder.create_vector(&[x, y]);

    // Note that, for convenience, it is also valid to create a vector of
    // references to structs, like this:
    // let path = builder.create_vector(&[&x, &y]);

    // Create the monster using the `Monster::create` helper function. This
    // function accepts a `MonsterArgs` struct, which supplies all of the data
    // needed to build a `Monster`. To supply empty/default fields, just use the
    // Rust built-in `Default::default()` function, as demonstrated below.
    let orc = Monster::create(&mut builder, &MonsterArgs{
        pos: Some(&Vec3::new(1.0f32, 2.0f32, 3.0f32)),
        mana: 150,
        hp: 80,
        name: Some(name),
        inventory: Some(inventory),
        color: Color::Red,
        weapons: Some(weapons),
        equipped_type: Equipment::Weapon,
        equipped: Some(axe.as_union_value()),
        //path: Some(path),
        ..Default::default()
    });

    // Serialize the root of the object, without providing a file identifier.
    builder.finish(orc, None);

    // We now have a FlatBuffer we can store on disk or send over a network.

    // ** file/network code goes here :) **

    // Instead, we're going to access it right away (as if we just received it).
    // This must be called after `finish()`.
    let buf = builder.finished_data(); // Of type `&[u8]`
    
    // Get access to the root:
    let monster = flatbuffers::root::<Monster>(buf).unwrap();

    // Get and test some scalar types from the FlatBuffer.
    let hp = monster.hp();
    let mana = monster.mana();
    let name = monster.name();

    assert_eq!(hp, 80);
    assert_eq!(mana, 150);  // default
    assert_eq!(name, Some("Orc"));    

    println!("The Monsters FlatBuffer was successfully created and accessed!");
    //dbg!(monster);    
}

fn user() {
    let mut builder = flatbuffers::FlatBufferBuilder::with_capacity(1024);
    let name = builder.create_string("Arthur Dent");
    let arthur = User::create(&mut builder, &UserArgs{
        name: Some(name),
        id: 42,
        ..Default::default()
    });
    builder.finish(arthur, None);
    let buf = builder.finished_data();
    let arthur = flatbuffers::root::<User>(buf).unwrap();
    let name = arthur.name();
    let id = arthur.id();
    assert_eq!(name, Some("Arthur Dent"));
    assert_eq!(id, 42);
    println!("The Users FlatBuffer was successfully created and accessed!");
    dbg!(arthur);
}

fn classification() {
}

fn test_base64_decoding() {
    //use data_encoding;
    use ascii_converter::*;
    use data_encoding::BASE64;
    let data = b"SGVsbG8gd29ybGQ=";
    let mut input = vec![0; BASE64.decode_len(data.len()).unwrap()];
    let len = BASE64.decode_mut(data, &mut input).unwrap();
    match decimals_to_string(&(input[0 .. len].to_vec())){
        Ok(num) => println!("* Output: {}", num),
        Err(e) => println!("* Error: {}", e),
    };
}

fn main() {
    //monster();
    //user();
    //classification();
    test_base64_decoding();
}
