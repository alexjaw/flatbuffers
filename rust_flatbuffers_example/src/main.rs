#![allow(dead_code)]
extern crate flatbuffers;

mod myschema_generated;
pub use myschema_generated::users::{
    User, UserArgs
};

mod classification_generated;
pub use classification_generated::dnn_vision::{
    GeneralClassification, GeneralClassificationArgs,
    ClassificationData, ClassificationDataArgs,
    ClassificationTop, ClassificationTopArgs,
};

#[allow(dead_code)]
fn test_file_io() {
    use std::fs::File;
    use std::io::prelude::*;
    use std::path::Path;

    let mut path = Path::new("test.bin");
    let display = path.display();
    let mut file = match File::create(&path) {
        Err(why) => panic!("couldn't create {}: {}", display, why),
        Ok(file) => file,
    };

    let mut buf = [0u8; 8];
    match file.write_all(&buf) {
        Err(why) => panic!("couldn't write to {}: {}", display, why),
        Ok(_) => println!("successfully wrote to {}", display),        
    }

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read the file contents into a string, returns `io::Result<usize>`
    //let mut s = String::new();
    let mut buf = [0u8, 8];
    match file.read_exact(&mut buf) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => print!("Ok\n"),
    }   

}

#[allow(dead_code)]
fn monster2() {
}

#[allow(dead_code)]
fn monster() {
    // import the generated code
    #[allow(dead_code, unused_imports)]
    #[path = "./monster_generated.rs"]
    mod monster_generated;
    pub use monster_generated::my_game::sample::{root_as_monster,
                                                Color, Equipment,
                                                Monster, MonsterArgs,
                                                Vec3,
                                                Weapon, WeaponArgs
    };
    let mut builder = flatbuffers::FlatBufferBuilder::new_with_capacity(1024);
    
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

    // Create the path vector of Vec3 objects.
    let x = Vec3::new(1.0, 2.0, 3.0);
    let y = Vec3::new(4.0, 5.0, 6.0);
    let path = builder.create_vector(&[x, y]);
    
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
        path: Some(path),
        ..Default::default()
    });

    // Call `finish()` to instruct the builder that this monster is complete.
    builder.finish(orc, None);

    // This must be called after `finish()`.
    // `finished_data` returns a byte slice.
    let buf = builder.finished_data(); // Of type `&[u8]`    
    
    let monster = monster_generated::my_game::
    let hp = monster.hp();
    dbg!(hp);
}

#[allow(dead_code)]
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

#[allow(dead_code)]
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

#[allow(dead_code)]
fn test_deserialize_classification() {
    use data_encoding::BASE64;
    let data = b"DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAABQAAAEwAAAA0AAAAJAAAABQAAAAEAAAA0P///4sCAAAAAHA93P///18AAAAAAJg96P///5kDAAAAAPg99P///3MCAAAAAPg9CAAMAAQACAAIAAAAUQIAAAAA+D0=";
    
    //base64 decode
    //let buf_decode = 
    let mut buf_decode = vec![0; BASE64.decode_len(data.len()).unwrap()];
    let len = BASE64.decode_mut(data, &mut buf_decode).unwrap();
    
    // Unwrap ClassificationTop
    let detections = flatbuffers::root::<ClassificationTop>(&buf_decode).unwrap();

    // Get perception
    let perception = detections.perception();

    // Get length: ClassificationListLength


    // Loop through ClassificationList, get classid and score
    //for i in 0..5 {
        //let classification = ???;
    //}
}

fn main() {
    monster();
    //monster2();
    //user();
    //classification();
    //test_base64_decoding();
    //test_deserialize_classification();
}
